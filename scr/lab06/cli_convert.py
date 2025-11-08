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