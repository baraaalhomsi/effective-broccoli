import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from collections import Counter

try:
    from src.lab04.io_txt_csv import read_text, write_csv
    from src.lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    import csv
    import re
    from collections import defaultdict

    def read_text(path, encoding="utf-8"):

        file_path = Path(path)
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()

    def write_csv(rows, path, header=None):

        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if rows:
            expected_len = len(rows[0])
            for i, row in enumerate(rows):
                if len(row) != expected_len:
                    raise ValueError(f"Row {i} has {len(row)} items, expected {expected_len}")

        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(header)
            writer.writerows(rows)

    def normalize(text: str, *, casefold: bool = True, yo_to_e: bool = True) -> str:

        if not text:
            return ""

        processed = text
        if casefold:
            processed = processed.casefold()
        if yo_to_e:
            processed = processed.replace('ё', 'е').replace('Ё', 'Е')

        processed = re.sub(r'[\t\r\n\v\f]+', ' ', processed)
        processed = re.sub(r' +', ' ', processed).strip()

        return processed

    def tokenize(text: str) -> List[str]:

        if not text:
            return []
        token_pattern = r'[a-zа-яё0-9_]+(?:-[a-zа-яё0-9_]+)*'
        return re.findall(token_pattern, text, flags=re.IGNORECASE)

    def count_freq(tokens: List[str]) -> Dict[str, int]:

        counter = defaultdict(int)
        for t in tokens:
            counter[t] += 1
        return dict(counter)

    def top_n(freq_dict: Dict[str, int], limit: int = 5) -> List[Tuple[str, int]]:

        sorted_items = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
        return sorted_items[:limit]


# === Processing functions ===

def process_text(text: str) -> Dict[str, int]:
    normalized = normalize(text)
    tokens = tokenize(normalized)
    return count_freq(tokens)


def print_summary(word_freq: Dict[str, int], total_words: int):
    unique_words = len(word_freq)
    top_words = top_n(word_freq, 5)

    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print("Top 5 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")


def print_pretty_table(word_freq: Dict[str, int]):
    if not word_freq:
        print("No data to display.")
        return

    sorted_words = top_n(word_freq, len(word_freq))
    max_word_len = max(len(word) for word in word_freq.keys())
    max_count_len = max(len(str(count)) for count in word_freq.values())

    word_col = max(max_word_len, len("Word"))
    count_col = max(max_count_len, len("Count"))

    print("\n" + "=" * (word_col + count_col + 5))
    print(f"{'Word':<{word_col}} | {'Count':>{count_col}}")
    print("=" * (word_col + count_col + 5))

    for word, count in sorted_words:
        print(f"{word:<{word_col}} | {count:>{count_col}}")

    print("=" * (word_col + count_col + 5))


def main_single(input_file: str, output_file: str, encoding: str = "utf-8"):

    try:
        text = read_text(input_file, encoding)
        word_freq = process_text(text)
        total_words = sum(word_freq.values())
        sorted_words = top_n(word_freq, len(word_freq))
        rows = [(word, str(count)) for word, count in sorted_words]
        write_csv(rows, output_file, header=("word", "count"))

        print_summary(word_freq, total_words)
        print_pretty_table(word_freq)
        print(f"\nReport saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Invalid file encoding. Try using --encoding cp1251.")
        sys.exit(1)


def main_multiple(input_files: List[str], per_file_output: str, total_output: str, encoding: str = "utf-8"):

    all_freq = {}
    per_file_data = []

    for file in input_files:
        try:
            text = read_text(file, encoding)
            word_freq = process_text(text)

            for word, count in word_freq.items():
                all_freq[word] = all_freq.get(word, 0) + count
                per_file_data.append((Path(file).name, word, str(count)))

        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Error: Invalid encoding in file '{file}'. Try using --encoding cp1251.")
            sys.exit(1)

    per_file_data.sort(key=lambda x: (x[0], -int(x[2]), x[1]))
    write_csv(per_file_data, per_file_output, header=("file", "word", "count"))

    sorted_total = top_n(all_freq, len(all_freq))
    total_rows = [(word, str(count)) for word, count in sorted_total]
    write_csv(total_rows, total_output, header=("word", "count"))

    total_words = sum(all_freq.values())
    print_summary(all_freq, total_words)
    print_pretty_table(all_freq)

    print(f"\nPer-file report saved to: {per_file_output}")
    print(f"Total summary report saved to: {total_output}")


def main():
    parser = argparse.ArgumentParser(description='Word frequency report generator.')
    parser.add_argument('--in', dest='input_files', nargs='+',
                        default=['data/lab04/input.txt'],
                        help='Input file(s). Default: data/lab04/input.txt')
    parser.add_argument('--out', dest='output_file',
                        default='data/lab04/report.csv',
                        help='Output CSV file for single-file mode.')
    parser.add_argument('--per-file', dest='per_file_output',
                        help='Output CSV file for per-file report.')
    parser.add_argument('--total', dest='total_output',
                        help='Output CSV file for total report.')
    parser.add_argument('--encoding', default='utf-8',
                        help='File encoding. Default: utf-8.')

    args = parser.parse_args()

    if len(args.input_files) == 1 and not args.per_file_output and not args.total_output:
        main_single(args.input_files[0], args.output_file, args.encoding)
    else:
        per_file = args.per_file_output or 'data/lab04/report_per_file.csv'
        total_file = args.total_output or 'data/lab04/report_total.csv'
        main_multiple(args.input_files, per_file, total_file, args.encoding)


if __name__ == "__main__":
    main()