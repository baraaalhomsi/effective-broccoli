import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))

from scr.lib.text import normalize, tokenize, count_freq, top_n


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

    table_output = os.getenv("TEXT_STATS_TABLE", "0") == "1"

    if "--table" in sys.argv or "-t" in sys.argv:
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
