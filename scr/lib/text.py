import re
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not text:
        return ""

    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")

    control_chars = ["\t", "\r", "\n", "\v", "\f"]
    for char in control_chars:
        text = text.replace(char, " ")

    text = re.sub(r"\s+", " ", text)
    text = text.strip()

    return text


def tokenize(text: str) -> List[str]:

    if not text:
        return []

    pattern = r"[\w]+(?:-[\w]+)*"

    tokens = re.findall(pattern, text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:

    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:

    items = list(freq.items())

    items.sort(key=lambda x: (-x[1], x[0]))

    return items[:n]


if __name__ == "__main__":
    print("===normalize===")
    print(normalize("ПрИвЕт\nМир\t"))
    print(normalize("ёжик, Ёлка"))
    print(normalize("Hello\r\nWorld"))
    print(
        normalize(
            "  двойные   пробелы  ",
        ),
        "\n",
    )

    print("===tokenizee===")
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"), "\n")

    print("===count_freq + top_n===")
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    print(freq)
    print(top_n(freq, n=2))
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    print(freq2)
    print(top_n(freq2, n=2), "\n")
