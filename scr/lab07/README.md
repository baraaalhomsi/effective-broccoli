# Лабораторная работа 7: Тестирование (pytest) + стиль (black)

## заданиe A: Тесты для scr\lib\text.py

```python
import pytest
from scr.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("Привет\nМир\t", "привет мир"),
            ("ежик, Елка", "ежик, елка"),
            ("Hello\n\nWorld", "hello world"),
            ("  двойные  пробелы  ", "двойные пробелы"),
            ("Hello\v\nworld", "hello world"),
            ("", ""),
            ("   ", ""),
        ],
    )
    def test_normalize_basic(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("hello world", ["hello", "world"]),
            ("привет мир", ["привет", "мир"]),
            ("one,two three", ["one", "two", "three"]),
            ("", []),
            ("   ", []),
            ("hello   world", ["hello", "world"]),
        ],
    )
    def test_tokenize_basic(self, source, expected):
        assert tokenize(source) == expected


class TestCountFreq:

    def test_count_freq_basic(self):
        tokens = ["hello", "world", "hello", "test"]
        result = count_freq(tokens)
        expected = {"hello": 2, "world": 1, "test": 1}
        assert result == expected

    def test_count_freq_empty(self):
        assert count_freq([]) == {}

    def test_count_freq_case_sensitive(self):
        tokens = ["Hello", "hello", "HELLO"]
        result = count_freq(tokens)
        expected = {"Hello": 1, "hello": 1, "HELLO": 1}
        assert result == expected


class TestTopN:

    def test_top_n_basic(self):
        freq = {"hello": 5, "world": 3, "test": 1}
        result = top_n(freq, 2)
        expected = [("hello", 5), ("world", 3)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        # alphapitical
        freq = {"cat": 3, "apple": 3, "banana": 3, "dog": 1}
        result = top_n(freq, 3)
        expected = [("apple", 3), ("banana", 3), ("cat", 3)]
        assert result == expected

    def test_top_n_more_than_available(self):
        freq = {"hello": 5, "world": 3}
        result = top_n(freq, 5)
        expected = [("hello", 5), ("world", 3)]
        assert result == expected

    def test_top_n_empty(self):
        assert top_n({}, 5) == []

    def test_top_n_zero(self):
        freq = {"hello": 5, "world": 3}
        assert top_n(freq, 0) == []

def test_integration_workflow():
    text = "hello world hello test world hello"

    normalized = normalize(text)
    assert normalized == "hello world hello test world hello"

    tokens = tokenize(normalized)
    assert tokens == ["hello", "world", "hello", "test", "world", "hello"]

    freq = count_freq(tokens)
    assert freq == {"hello": 3, "world": 2, "test": 1}

    top_words = top_n(freq, 2)
    assert top_words == [("hello", 3), ("world", 2)]
```
![alt text](/images/lab07/Screenshot%202025-11-23%20183751.png)

## заданиe B: Тесты для scr\lab05\json_to-csv.py

```python
import pytest
import json
import csv
from pathlib import Path
from scr.lab05.json_to_csv import json_to_csv, csv_to_json


class TestJsonToCsv:

    def test_json_to_csv_basic(self, tmp_path: Path):

        scr = tmp_path / "test.json"
        dst = tmp_path / "test.csv"

        data = [
            {"name": "Alice", "age": 22, "city": "Moscow"},
            {"name": "Bob", "age": 25, "city": "London"},
        ]

        scr.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        json_to_csv(str(scr), str(dst))

        assert dst.exists()

        with dst.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 2
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "22"
        assert rows[1]["name"] == "Bob"

    def test_json_to_csv_empty_file(self, tmp_path: Path):
        scr = tmp_path / "empty.json"
        dst = tmp_path / "output.csv"

        scr.write_text("", encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(scr), str(dst))

    def test_json_to_csv_invalid_json(self, tmp_path: Path):
        scr = tmp_path / "invalid.json"
        dst = tmp_path / "output.csv"

        scr.write_text("{invalid json}", encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(scr), str(dst))

    def test_json_to_csv_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_csv_to_json_invalid_csv(self, tmp_path: Path):
        scr = tmp_path / "invalid.csv"
        dst = tmp_path / "output.json"

        csv_content = """name,age,city
Alice,22
Bob,25,London,ExtraColumn
"""

        scr.write_text(csv_content, encoding="utf-8")

        with pytest.raises(ValueError):
            csv_to_json(str(scr), str(dst))


class TestCsvToJson:

    def test_csv_to_json_basic(self, tmp_path: Path):

        scr = tmp_path / "test.csv"
        dst = tmp_path / "test.json"

        csv_content = """name,age,city
Alice,22,Moscow
Bob,25,London"""
        scr.write_text(csv_content, encoding="utf-8")

        csv_to_json(str(scr), str(dst))

        assert dst.exists()

        with dst.open(encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 2
        assert data[0] == {"name": "Alice", "age": "22", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "25", "city": "London"}

    def test_csv_to_json_empty_file(self, tmp_path: Path):
        scr = tmp_path / "empty.csv"
        dst = tmp_path / "output.json"

        scr.write_text("", encoding="utf-8")

        with pytest.raises(ValueError):
            csv_to_json(str(scr), str(dst))


class TestRoundTrip:

    def test_json_to_csv_to_json_roundtrip(self, tmp_path: Path):

        original_data = [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25},
        ]

        json_scr = tmp_path / "original.json"
        csv_file = tmp_path / "converted.csv"
        json_dst = tmp_path / "final.json"

        json_scr.write_text(
            json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
        )

        json_to_csv(str(json_scr), str(csv_file))

        csv_to_json(str(csv_file), str(json_dst))

        with json_dst.open(encoding="utf-8") as f:
            final_data = json.load(f)

        assert len(final_data) == len(original_data)
        assert final_data[0]["name"] == original_data[0]["name"]
        assert final_data[1]["name"] == original_data[1]["name"]
```

![alt text](/images/lab07/Screenshot%202025-11-23%20183841.png)

## два теста вместе взятые

![alt text](/images/lab07/Screenshot%202025-11-23%20183921.png)

## Задание С: Стиль коде (black)

![alt text](/images/lab07/Screenshot%202025-11-23%20184418.png)

## Дополнительное задание: покрытие куда

![alt text](/images/lab07/Screenshot%202025-12-03%20202335.png)

![alt text](/images/lab07/Screenshot%202025-12-03%20202310.png)

![alt text](/images/lab07/Screenshot%202025-12-03%20202408.png)


