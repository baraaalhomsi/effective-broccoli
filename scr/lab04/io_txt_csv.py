from pathlib import Path
import csv
from typing import Union, Tuple, List


def read_text_file(path: Union[str, Path], encoding: str = "utf-8") -> str:

    file_path = Path(path)

    with open(file_path, "r", encoding=encoding) as f:
        return f.read()


def save_to_csv(
    data: List[Union[tuple, list]],
    path: Union[str, Path],
    header: Tuple[str, ...] = None,
) -> None:

    file_path = Path(path)
    make_parent_dir(file_path)

    if data:
        expected_len = len(data[0])
        for i, row in enumerate(data):
            if len(row) != expected_len:
                raise ValueError(
                    f"Row {i} has length {len(row)}, expected {expected_len}"
                )

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")

        if header:
            writer.writerow(header)

        writer.writerows(data)


def make_parent_dir(path: Union[str, Path]) -> None:

    dir_path = Path(path).parent
    dir_path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    try:
        text = read_text_file("data/lab04/input.txt")
        print(f"File content: '{text}'")
        print(f"Content length: {len(text)}")
    except Exception as e:
        print(f"[Error reading text file] {e}")

    try:
        save_to_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
        print("CSV file 'check.csv' created successfully.")
    except Exception as e:
        print(f"[Error writing CSV] {e}")
