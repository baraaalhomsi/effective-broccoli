# Лабораторная работа 3 - Тексты и частоты слов

## Описание
Реализация модуля для обработки текста и анализа частот слов с поддержкой табличного вывода.

## Структура проекта

```
src/
├── lib/
│   └── text.py           # Модуль с функциями для работы с текстом
└── lab03/
    ├── text_stats.py      # Скрипт для анализа текста из stdin
    └── README.md          # Этот файл
```

### заданиe A
```python
import re
from typing import Dict, List, Tuple

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not text:
        return ""

    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')

    control_chars = ['\t', '\r', '\n', '\v', '\f']
    for char in control_chars:
        text = text.replace(char, ' ')

    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def tokenize(text: str) -> List[str]:

    if not text:
        return []

    pattern = r'[\w]+(?:-[\w]+)*'
    
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
    print(normalize("  двойные   пробелы  ",),"\n")

    print("===tokenizee===")
    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"),"\n")

    print("===count_freq + top_n===")
    freq=count_freq(["a","b","a","c","b","a"])
    print(freq)
    print(top_n(freq, n=2))
    freq2=count_freq(["bb","aa","bb","aa","cc"])
    print(freq2)
    print(top_n(freq2, n=2),"\n")
```

![alt text](/images/lab03/A.png)

### заданиe B
```python
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text import normalize, tokenize, count_freq, top_n

def process_text(text: str, table_output: bool = False) -> str:

    if not text.strip():
        return "No input text provided."

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, 5)

    output_lines = []
    output_lines.append(f"Всего слов: {len(tokens)}")
    output_lines.append(f"Уникальных слов: {len(frequencies)}")
    output_lines.append("Топ-5:")
    
    if table_output:

        if top_words:
            
            max_word_len = max(len(word) for word, _ in top_words)
            max_word_len = max(max_word_len, len("слово"))
            
            header_word = "слово".ljust(max_word_len)
            output_lines.append(f"| {header_word} | частота |")
            output_lines.append(f"|{'-' * (max_word_len + 2)}|---------|")

            for word, freq in top_words:
                padded_word = word.ljust(max_word_len)
                output_lines.append(f"| {padded_word} | {freq:7} |")
        else:
            output_lines.append("| (нет данных) |         |")
    else:
        
        for word, freq in top_words:
            output_lines.append(f"{word}:{freq}")
    
    return "\n".join(output_lines)

def main():

    table_output = os.getenv('TEXT_STATS_TABLE', '0') == '1'

    if '--table' in sys.argv or '-t' in sys.argv:
        table_output = True

    if sys.stdin.isatty():
        
        print("Введите текст (Ctrl+Z затем Enter для завершения ввода на Windows):")
        print("Для табличного вывода используйте: --table или -t")
    
    try:
        input_text = sys.stdin.read().strip()
    except KeyboardInterrupt:
        print("\nВвод прерван.")
        return
    
    if not input_text:
        print("Ошибка: Не получен входной текст.")
        sys.exit(1)

    result = process_text(input_text, table_output)
    print(result)

if __name__ == "__main__":
    main()
```

![alt text](/images/lab03/B.png)