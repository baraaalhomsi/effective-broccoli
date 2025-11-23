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
