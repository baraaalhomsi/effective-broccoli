# effective-broccoli

## Lab1

### ex01

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![alt text](./images/lab01/image.png)

### ex02

```python
print("inter the first number:")
a=float(input())
print("inter the second number:")
b=float(input())
sum=a+b
avg=(a*b)/2
print("sum= ",f"{sum:.2f}")
print("avg= ",f"{avg:.2f}")
```

![alt text](./images/lab01/image-1.png)

### ex03

```python
print("enter the price : ")
price=float(input())
print("enter the discount %: ")
discount=float(input())
print("enter the vat %: ")
vat=float(input())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print("price after discount: ",f"{base:.2f}")
print("vat_amount: ",f"{vat_amount:.2f}")
print("the final price: ",f"{total:.2f}")
```

![alt text](./images/lab01/image-2.png)

### ex04

```python
print("enter how many minutes: ")
a=int(input())
b=a//60
c=a%60
if b<=23:
    print(f"{b:02}:{c:02}")
else:
     b=b-24
     print(f"{b:02}:{c:02}")
 ```

 ![alt text](./images/lab01/image-3.png)  ![alt text](./images/lab01/image-4.png)

 ### ex05

 ```python
print("your name is: ")
name=str(input())
def first_letters(names):
    nnn=name.split()
    the_basic_part= [n[0] for n in nnn if n]
    return '.'.join(the_basic_part)
length=len(name.replace(" ", ""))
print("short name:",first_letters(name))
print("length(symbols):",length)
```

![alt text](./images/lab01/imagee.png)

### ex06

```python
n = int(input())
ochno=0
zaochno=0
for _ in range(n):
    surname, name, age, form = input().split()
    if form == "True":
        ochno+=1
    else:
        zaochno+=1
print(ochno, zaochno)
```

![alt text](./images/lab01/image-6.png)

## Lab2

### array

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("the array cannot be empty")
    min_val = nums[0]
    max_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return (min_val, max_val)
print("min_max: ")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
try:
    print(min_max([]))
except Exception as e:
    print(f"ValueErorre: {e}\n")

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = list(set(nums))
    unique_nums.sort()
    return unique_nums

print("unique_sorted: ")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]),"\n")

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list, tuple)):
            raise TypeError("ab is not list or tuple")
        for element in item:
            if isinstance(element, (list, tuple)):
                result.extend(flatten([element]))
            else:
                result.append(element)
    return result

print("flatten: ")
print(flatten([[1, 2], [3, 4]]))
print(flatten([([1, 2], (3, 4, 5))]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except Exception as e:
    print(f"TybeErorre: {e}")
```

![alt text](./images/lab02/array.png)

### matrix

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    cols=len(mat[0])
    rows=len(mat)
    transpose=[]
    for i, row in enumerate(mat):
        if len(row) != cols:
            raise ValueError("рваная матрица")
    for col_index in range(cols):
        new_row=[]
        for row_index in range(rows):
            new_row.append(mat[row_index][col_index])
        transpose.append(new_row)
    return transpose

print("transpose: ")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[]]))
try:
    print(transpose([[1, 2], [3]]))
except Exception as e:
    print(f"ValueError: {e}","\n")

def row_sums(mat: list[list[float | int]]) -> list[float]:
    cols=len(mat[0])
    rows=len(mat)
    new_mat=[]
    for i, row in enumerate(mat):
        if len(row) != cols:
            raise ValueError("рваная матрица")
    for num_row in range (rows):
        row_sum=0
        for num_col in range (cols):
            row_sum+=mat[num_row][num_col]
        new_mat.append(row_sum)
    return new_mat

print("row_sums: ")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
try:
    print(row_sums([[1, 2], [3]]))
except Exception as e:
    print(f"ValueError: {e}","\n")

def col_sums(mat: list[list[float | int]]) -> list[float]:
    cols=len(mat[0])
    rows=len(mat)
    new_mat=[]
    for i, row in enumerate(mat):
        if len(row) != cols:
            raise ValueError("рваная матрица")
    for num_col in range (cols):
        col_sum=0
        for num_row in range (rows):
            col_sum+=mat[num_row][num_col]
        new_mat.append(col_sum)
    return new_mat

print("col_sums: ")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
try:
    print(col_sums([[1, 2], [3]]) )
except Exception as e:
    print(f"ValueError: {e}")
```

![alt text](./images/lab02/matrix.png)

### tuples

```python
def format_record(record):
    if type(record) != tuple:
        raise TypeError("Input must be a tuple")
    if len(record) != 3:
        raise ValueError("Tuple must have exactly 3 elements")
    full_name, group, gpa = record
    if type(full_name) != str:
        raise TypeError("ФИО must be a string")
    if type(group) != str:
        raise TypeError("Group must be a string")
    if type(gpa) not in (int, float):
        raise TypeError("GPA must be a number")
    full_name = full_name.strip()
    if not full_name:
        raise ValueError("ФИО cannot be empty")
    group = group.strip()
    if not group:
        raise ValueError("Group cannot be empty")
    if gpa < 0:
        raise ValueError("GPA cannot be negative")
    name_parts = [part.strip() for part in full_name.split() if part.strip()]
    if len(name_parts) < 2:
        raise ValueError("ФИО must contain at least last name and first name")
    last_name = name_parts[0]
    first_names = name_parts[1:]
    initials = '.'.join(name[0].upper() for name in first_names) + '.'
    formatted_gpa = f"{gpa:.2f}"
    formatted_result = f"{last_name} {initials}, гр. {group}, GPA {formatted_gpa}"
    return formatted_result
print("=== format_record ===")   
print(format_record(("Иванов Иван Иванович", "БИВТ-25", 4.6)))  
print(format_record(("Петров Пётр", "IKB0-12", 5.0)))  
print(format_record(("Петров Пётр Петрович", "IKB0-12", 5.0)))
print(format_record(("Сидорова анна аергеевна", "АВВ-01", 3.999)))
```

![alt text](./images/lab02/tuples.png)

## Lab04

### Файлы: TXT/CSV и отчёты по текстовой статистике

### Структура проекта
```
python_labs/
 ├──src/
 │├── lib/
 ││   └── text.py
 │└── lab04/
 │├── io_txt_csv.py
 │└── text_report_advanced.py
 ├──data/
 │├── lab04/
 │├── input.txt
 │├── a.txt
 │└── b.txt
 ```

 ### Задание A — модуль src/lab04/io_txt_csv.py

 ```python
 from pathlib import Path
import csv
from typing import Union, Tuple, List


def read_text_file(path: Union[str, Path], encoding: str = "utf-8") -> str:

    file_path = Path(path)
    
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()


def save_to_csv(data: List[Union[tuple, list]], path: Union[str, Path], 
                header: Tuple[str, ...] = None) -> None:

    file_path = Path(path)
    make_parent_dir(file_path)
    
    if data:
        expected_len = len(data[0])
        for i, row in enumerate(data):
            if len(row) != expected_len:
                raise ValueError(f"Row {i} has length {len(row)}, expected {expected_len}")
    
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        
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
```

![alt text](/images/lab04/image1.png)  ![alt text](/images/lab04/image10.png)

![alt text](/images/lab04/image3.png)  ![alt text](/images/lab04/image2.png)

### Задание B — скрипт src/lab04/text_report_advanced.py

```python
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

from scr.lb04.io_txt_csv import read_text_file, save_to_csv
from scr.lib.text import normalize, tokenize, count_freq, top_n

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
        text = read_text_file(input_file, encoding)
        word_freq = process_text(text)
        total_words = sum(word_freq.values())

        sorted_words = top_n(word_freq, len(word_freq))
        rows = [(word, str(count)) for word, count in sorted_words]
        save_to_csv(rows, output_file, header=("word", "count"))

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

    all_freq: Dict[str, int] = {}
    per_file_data = []

    for file in input_files:
        try:
            text = read_text_file(file, encoding)
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
    save_to_csv(per_file_data, per_file_output, header=("file", "word", "count"))

    sorted_total = top_n(all_freq, len(all_freq))
    total_rows = [(word, str(count)) for word, count in sorted_total]
    save_to_csv(total_rows, total_output, header=("word", "count"))

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
```
### into the terminal
"python scr/lab04/text_report_advanced.py --in data/lab04/a.txt data/lab04/b.txt --per-file data/lab04/report_per_file.csv --total data/lab04/report_total.csv"

![alt text](/images/lab04/image4.png)  ![alt text](/images/lab04/image5.png)

![alt text](/images/lab04/image6.png)  ![alt text](/images/lab04/image7.png)
![alt text](/images/lab04/image8.png)   

### by click "Run"(works with file input.txt)
![alt text](/images/lab04/image9.png)

## lab05

### JSON и конвертации (JSON↔CSV, CSV→XLSX): Техническое задание

### Задание A — JSON ↔ CSV

```python
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:

    if not Path(json_path).exists():
        raise FileNotFoundError(f"file {json_path} is not exist")

    try:
        with open(json_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError:
        raise ValueError("file JSON uncorrect")

    if not data:
        raise ValueError("file JSON is empty")

    if not isinstance(data, list):
        raise ValueError("JSON must to be a list")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("all data in JSON must to be dictionary")
    
    # to creat the fail if it is not not exist
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        if data:
            # getting column names (the keys of the first dictionary)
            fieldnames = list(data[0].keys())
            
            # arrengment of columns(alphabetical) 
            fieldnames.sort()
            
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            
            # writing data (complete data)
            for row in data:
            
                complete_row = {field: row.get(field, "") for field in fieldnames}
                writer.writerow(complete_row)


def csv_to_json(csv_path: str, json_path: str) -> None:

    if not Path(csv_path).exists():
        raise FileNotFoundError(f"file {csv_path} is not exict")

    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
    except Exception as e:
        raise ValueError(f"wrong while reading CSV: {e}")

    if not data:
        raise ValueError("file CSV is empty")
    
    # to creat the fail if it is not not exist
    Path(json_path).parent.mkdir(parents=True, exist_ok=True)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)


def main():
    try:

        print("converting people.json to CSV...")
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
        print("the conversion was successful: people_from_json.csv")

        print("converting people.csv to JSON...")
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print("the conversion was successful: people_from_csv.json")
        
    except Exception as e:
        print(f"wrong: {e}")


if __name__ == "__main__":
    main()
```

![alt text](/images/lab05/A1.png)
![alt text](/images/lab05/A2.png)
![alt text](/images/lab05/A3.png)

### Задание B — CSV → XLSX

```python
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:

    if not Path(csv_path).exists():
        raise FileNotFoundError(f"file {csv_path} is not exist")

    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
    except Exception as e:
        raise ValueError(f"wrong while reading CSV: {e}")

    if not rows:
        raise ValueError("file CSV is empty")
    
    # to creat the fail if it is not not exist
    Path(xlsx_path).parent.mkdir(parents=True, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # copy info from CSV to Exel
    for row in rows:
        ws.append(row)
    
    # adjusting width of the colmuns
    for col_num, column in enumerate(ws.columns, 1):
        max_length = 0
        
        # the longest text in te column
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        # adjusting width
        adjusted_width = max(8, min(max_length + 2, 50))
        col_letter = get_column_letter(col_num)
        ws.column_dimensions[col_letter].width = adjusted_width

    wb.save(xlsx_path)

def main():

    try:
        print("converting people.csv to XLSX...")
        csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
        print("the conversion was successful: people.xlsx")
        
        print("converting cities.csv to XLSX...")
        csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
        print("the conversion was successful: cities.xlsx")
        
    except Exception as e:
        print(f"wrong: {e}")


if __name__ == "__main__":
    main()
```

![alt text](/images/lab05/B1.png)
![alt text](/images/lab05/B2.png)
![alt text](/images/lab05/B3.png)

## lab06 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры): Техническое задание

### 1- reading and printing the text \ or counting and frequency of word (cli_text.py)

```python
import argparse
import sys
from pathlib import Path
from scr.lib.text import normalize, tokenize, count_freq, top_n

def read_file_lines(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def cat_command(input_file, number_lines=False):

    lines = read_file_lines(input_file)
    
    for i, line in enumerate(lines, 1):
        if number_lines:
            print(f"{i:6d}.\t{line.rstrip()}")
        else:
            print(line.rstrip())

def stats_command(input_file, n=5):

    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    frequencies = count_freq(tokens)
    top_words = top_n(frequencies, n)
    
    print(f"Top {n} most frequent words:")
    print("-" * 30)
    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i:2d}. {word:<8} :{count:3d} times")

def main():
    parser = argparse.ArgumentParser(description="Text processing tools - File display and word statistics")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    cat_parser = subparsers.add_parser("cat", help="Display file content")
    cat_parser.add_argument("--input", required=True, help="Input file path")
    cat_parser.add_argument("-n", action="store_true", help="Number lines")
    
    stats_parser = subparsers.add_parser("stats", help="Word frequency statistics")
    stats_parser.add_argument("--input", required=True, help="Input text file path")
    stats_parser.add_argument("--top", type=int, default=20, help="Number of top words (default: 20)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)

if __name__ == "__main__":
    main()
```
### for printing
"python -m scr.lab06.cli_text cat --input data/samples/people.csv **or** python -m scr.lab06.cli_text cat --input data/samples/people.csv -n"

![alt text](/images/lab06/1.png)

### for counting
"python -m scr.lab06.cli_text stats --input data/samples/people.txt --top 12"

![alt text](/images/lab06/2.png)

### 2- CLI‑конвертер

```python
import argparse
import sys
import os
from pathlib import Path
from scr.lab05.json_to_csv import json_to_csv, csv_to_json
from scr.lab05.csv_to_xlsx import csv_to_xlsx

def ensure_directory_exists(file_path):

    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def convert_json_to_csv(input_file, output_file):

    ensure_directory_exists(output_file)
    json_to_csv(input_file, output_file)
    print(f"Successfully converted: {input_file} → {output_file}")

def convert_csv_to_json(input_file, output_file):

    ensure_directory_exists(output_file)
    csv_to_json(input_file, output_file)
    print(f"Successfully converted: {input_file} → {output_file}")

def convert_csv_to_xlsx(input_file, output_file):

    ensure_directory_exists(output_file)
    csv_to_xlsx(input_file, output_file)
    print(f"Successfully converted: {input_file} → {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Data conversion tools between different formats")
    subparsers = parser.add_subparsers(dest="command", help="Available conversion commands")

    json2csv_parser = subparsers.add_parser("json2csv", help="Convert JSON to CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Input JSON file")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Output CSV file")

    csv2json_parser = subparsers.add_parser("csv2json", help="Convert CSV to JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Input CSV file")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Output JSON file")

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Input CSV file")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Output XLSX file")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "json2csv":
        convert_json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        convert_csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        convert_csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()
```

### json to csv
"python -m scr.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv"
### csv to json
"python -m scr.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json"
### csv to xlsx
"python -m scr.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx"

![alt text](/images/lab06/3.png)

## ЛР9 — «База данных» на CSV: класс Group, CRUD-операции и CLI

### scr/lab09/group.py

```python
import csv
import sys
import os
from pathlib import Path
from typing import List, Optional

current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.append(str(project_root))

try:
    from lab08.models import Student
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    exit(1)


class Group:
    
    def __init__(self, storage_path: str):

        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:

        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self) -> List[dict]:

        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_all(self, rows: List[dict]) -> None:

        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['fio', 'birthdate', 'group', 'gpa']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:

        rows = self._read_all()
        students = []
        for row in rows:
            try:

                row['gpa'] = float(row['gpa'])
                student = Student(**row)
                students.append(student)
            except (ValueError, TypeError) as e:
                print(f"Warning: Error converting row data: {row} - {e}")
                continue
        return students
    
    def add(self, student: Student) -> None:

        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])
    
    def find(self, substr: str) -> List[Student]:

        rows = self._read_all()
        matching_rows = [r for r in rows if substr.lower() in r["fio"].lower()]
        
        students = []
        for row in matching_rows:
            try:
                row['gpa'] = float(row['gpa'])
                student = Student(**row)
                students.append(student)
            except (ValueError, TypeError) as e:
                print(f"Warning: Error converting row data: {row} - {e}")
                continue
        return students
    
    def remove(self, fio: str) -> bool:

        rows = self._read_all()
        initial_count = len(rows)

        rows = [r for r in rows if r["fio"] != fio]
        
        if len(rows) < initial_count:
            self._write_all(rows)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
 
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:

                for field, value in fields.items():
                    if field in ['fio', 'birthdate', 'group', 'gpa']:
                        row[field] = str(value)
                updated = True
        
        if updated:
            self._write_all(rows)
        return updated
    
    # ★ Bonus Task (Optional)
    def stats(self) -> dict:

        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }

        gpas = [s.gpa for s in students]
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = sum(gpas) / len(gpas)

        groups = {}
        for student in students:
            group = student.group
            groups[group] = groups.get(group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]]
        
        return {
            "count": len(students),
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": round(avg_gpa, 2),
            "groups": groups,
            "top_5_students": top_5
        }
```

### scr/lab09/test_group.py 

```python
import sys
import os
from pathlib import Path

current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.append(str(project_root))

try:
    from lab08.models import Student
    from group import Group
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    exit(1)

def main():

    data_path = "data/lab09/students.csv"

    group = Group(data_path)
    
    print("=" * 50)
    print("Testing Group Class - Student Data Management")
    print("=" * 50)
    
    # 1. Test adding students
    print("\n1. Adding new students:")
    
    students_to_add = [
        Student("Ahmed Mohamed", "2002-05-14", "SE-01", 4.5),
        Student("Sara Khalid", "2003-11-22", "SE-02", 3.8),
        Student("Mohamed Ahmed", "2001-07-30", "SE-01", 4.2),
        Student("Fatima Ali", "2002-12-10", "SE-02", 4.8),
        Student("Ali Hassan", "2003-03-25", "SE-03", 3.5),
        Student("Khalid Mohamed", "2002-08-15", "SE-01", 4.0),
    ]
    
    for student in students_to_add:
        group.add(student)
        print(f"  ✓ Added: {student.fio} - {student.group} - GPA: {student.gpa}")
    
    # 2. Test listing all students
    print("\n2. Listing all students:")
    all_students = group.list()
    for student in all_students:
        print(f"  - {student.fio} | {student.birthdate} | {student.group} | {student.gpa}")
    
    # 3. Test searching
    print("\n3. Searching for students with 'Mohamed' in name:")
    found_students = group.find("Mohamed")
    for student in found_students:
        print(f"  ✓ Found: {student.fio} - GPA: {student.gpa}")
    
    # 4. Test updating
    print("\n4. Updating Ahmed Mohamed's GPA to 4.7:")
    if group.update("Ahmed Mohamed", gpa=4.7):
        print("  ✓ GPA updated successfully")
    else:
        print("  ✗ Student not found")
    
    # 5. Test deleting
    print("\n5. Deleting student 'Ali Hassan':")
    if group.remove("Ali Hassan"):
        print("  ✓ Student deleted successfully")
    else:
        print("  ✗ Student not found")
    
    # 6. Show students after modifications
    print("\n6. Students after modifications:")
    updated_students = group.list()
    for student in updated_students:
        print(f"  - {student.fio} | {student.group} | GPA: {student.gpa}")
    
    # 7. Test statistics (if available)
    print("\n7. Group statistics:")
    try:
        stats = group.stats()
        print(f"  Student count: {stats['count']}")
        print(f"  Minimum GPA: {stats['min_gpa']}")
        print(f"  Maximum GPA: {stats['max_gpa']}")
        print(f"  Average GPA: {stats['avg_gpa']}")
        print(f"  Group distribution: {stats['groups']}")
        print("  Top 5 students:")
        for i, student in enumerate(stats['top_5_students'], 1):
            print(f"    {i}. {student['fio']} - GPA: {student['gpa']}")
    except AttributeError:
        print("  (Statistics feature not enabled)")
    
    print("\n" + "=" * 50)
    print("Test completed successfully!")
    print(f"Data saved to: {data_path}")
    print("=" * 50)

if __name__ == "__main__":
    main()
```

### into the terminal
" python scr/lab09/test_group.py"

![alt text](/images/lab09/Screenshot%202025-12-05%20201928.png)

![alt text](/images/lab09/Screenshot%202025-12-05%20201827.png)

## ЛР10 — Структуры данных: Stack, Queue, Linked List и бенчмарки

### Задание A. Stack и Queue (src/lab10/structures.py)

```python
from collections import deque
from typing import Any, Optional


class Stack:
    
    def __init__(self) -> None:

        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:

        self._data.append(item)
    
    def pop(self) -> Any:

        if self.is_empty():
            raise IndexError("not able to remove element from empty Stack")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:

        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:

        return len(self._data) == 0
    
    def __len__(self) -> int:
  
        return len(self._data)
    
    def __str__(self) -> str:
 
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
      
        return f"Stack({self._data})"


class Queue:
    
    def __init__(self) -> None:
 
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:

        self._data.append(item)
    
    def dequeue(self) -> Any:

        if self.is_empty():
            raise IndexError("not able to remove element from empty Queue")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]: # return the first element
   
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:

        return len(self._data) == 0
    
    def __len__(self) -> int:

        return len(self._data)
    
    def __str__(self) -> str:

        return f"Queue({list(self._data)})"
    
    def __repr__(self) -> str:

        return f"Queue({list(self._data)})"
```

### Задание B. SinglyLinkedList (src/lab10/linked_list.py)

```python
from typing import Any, Optional, Iterator

class Node:
    
    def __init__(self, value: Any) -> None:

        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __str__(self) -> str:

        return f"[{self.value}]"
    
    def __repr__(self) -> str:

        return f"Node({self.value})"


class SinglyLinkedList:
    
    def __init__(self) -> None:

        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:

        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:

        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:

        if idx < 0 or idx > self._size:
            raise IndexError(f"the index {idx} out of the range {self._size}]")
        
        if idx == 0:
            self.prepend(value)
        elif idx == self._size:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            self._size += 1
    
    def remove(self, value: Any) -> bool:

        if self.is_empty():
            return False
        
        # remove the first element
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # find the node that precedes the node to be remove
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # if there is not value
        if current.next is None:
            return False
        
        # remove the node
        current.next = current.next.next
        
        # uptade the tail if the last element was removed
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return True
    
    def remove_at(self, idx: int) -> Any:
 
        if idx < 0 or idx >= self._size:
            raise IndexError(f"the index {idx} out of the range {self._size - 1}]")
        
        if idx == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            removed_value = current.next.value
            current.next = current.next.next
            
            if current.next is None:
                self.tail = current
        
        self._size -= 1
        return removed_value
    
    def search(self, value: Any) -> bool:

        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def get(self, idx: int) -> Any:

        if idx < 0 or idx >= self._size:
            raise IndexError(f"the index {idx} out of the range {self._size - 1}]")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        
        return current.value
    
    def is_empty(self) -> bool:
 
        return self._size == 0
    
    def __iter__(self) -> Iterator[Any]:
   
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:

        return self._size
    
    def __str__(self) -> str:
     
        if self.is_empty():
            return "SinglyLinkedList([])"
        
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        
        return "SinglyLinkedList(" + " -> ".join(parts) + ")"
    
    def __repr__(self) -> str:
    
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def pretty_print(self) -> str:
       
        if self.is_empty():
            return "Empty List"
        
        result = []
        current = self.head
        while current is not None:
            result.append(f"[{current.value}]")
            current = current.next
        
        return " -> ".join(result) + " -> None"
```

### Using (scr\lab10\benchmark.py)

```python
import time
import random
from structures import Stack, Queue
from linked_list import SinglyLinkedList

def measure_time(func, *args):

    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def test_stack_performance():

    print("Testing Stack performance...")
    
    # Push test
    stack = Stack()
    start = time.perf_counter()
    for i in range(10000):
        stack.push(i)
    push_time = time.perf_counter() - start
    
    # Pop test
    start = time.perf_counter()
    for _ in range(10000):
        stack.pop()
    pop_time = time.perf_counter() - start
    
    print(f"  Push 10,000 items: {push_time:.4f}s")
    print(f"  Pop 10,000 items:  {pop_time:.4f}s")
    return push_time + pop_time


def test_queue_performance():

    print("Testing Queue performance...")
    
    queue = Queue()
    start = time.perf_counter()
    for i in range(10000):
        queue.enqueue(i)
    enqueue_time = time.perf_counter() - start
    
    start = time.perf_counter()
    for _ in range(10000):
        queue.dequeue()
    dequeue_time = time.perf_counter() - start
    
    print(f"  Enqueue 10,000 items: {enqueue_time:.4f}s")
    print(f"  Dequeue 10,000 items: {dequeue_time:.4f}s")
    return enqueue_time + dequeue_time


def test_linked_list_performance():

    print("Testing Linked List performance...")
    
    sll = SinglyLinkedList()
    
    # Append test
    start = time.perf_counter()
    for i in range(5000):
        sll.append(i)
    append_time = time.perf_counter() - start
    
    # Prepend test
    sll2 = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(5000):
        sll2.prepend(i)
    prepend_time = time.perf_counter() - start
    
    # Search test
    start = time.perf_counter()
    for i in range(100):
        sll.search(random.randint(0, 4999))
    search_time = time.perf_counter() - start
    
    print(f"  Append 5,000 items:  {append_time:.4f}s")
    print(f"  Prepend 5,000 items: {prepend_time:.4f}s")
    print(f"  Search 100 items:    {search_time:.4f}s")
    
    return append_time + prepend_time + search_time

def compare_all():
 
    print("\n" + "="*50)
    print("COMPARING ALL DATA STRUCTURES")
    print("="*50)
    
    # Test each structure
    stack_time = test_stack_performance()
    print()
    
    queue_time = test_queue_performance()
    print()
    
    ll_time = test_linked_list_performance()
    
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    
    print(f"\nTotal time for operations:")
    print(f"  Stack:          {stack_time:.4f}s")
    print(f"  Queue:          {queue_time:.4f}s")
    print(f"  Linked List:    {ll_time:.4f}s")
    
    print(f"\nRelative speed (lower is faster):")
    fastest = min(stack_time, queue_time, ll_time)
    print(f"  Stack:          {stack_time/fastest:.2f}x")
    print(f"  Queue:          {queue_time/fastest:.2f}x")
    print(f"  Linked List:    {ll_time/fastest:.2f}x")


def simple_example():

    print("\n" + "="*50)
    print("SIMPLE USAGE EXAMPLES")
    print("="*50)
    
    # Stack example
    print("\n1. Stack Example:")
    stack = Stack()
    stack.push("First")
    stack.push("Second")
    stack.push("Third")
    print(f"   Stack: {stack}")
    print(f"   Pop: {stack.pop()}")
    print(f"   Peek: {stack.peek()}")
    
    # Queue example
    print("\n2. Queue Example:")
    queue = Queue()
    queue.enqueue("Task 1")
    queue.enqueue("Task 2")
    queue.enqueue("Task 3")
    print(f"   Queue: {queue}")
    print(f"   Dequeue: {queue.dequeue()}")
    print(f"   Next: {queue.peek()}")
    
    # Linked List example
    print("\n3. Linked List Example:")
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.prepend(5)
    print(f"   List: {sll}")
    print(f"   Pretty: {sll.pretty_print()}")
    print(f"   Length: {len(sll)}")

def main():

    print("SIMPLE DATA STRUCTURE BENCHMARK")
    print("="*50)
    
    # Show examples
    simple_example()
    
    # Run comparison
    compare_all()
    
    print("\n" + "="*50)
    print("Benchmark Complete!")
    print("="*50)

if __name__ == "__main__":
    main()
```

### into the terminal

"python scr\lab10\benchmark.py"

![alt text](/images/lab10/Screenshot%202025-12-17%20223004.png)

![alt text](/images/lab10/Screenshot%202025-12-17%20230318.png)