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