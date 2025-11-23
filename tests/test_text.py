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
