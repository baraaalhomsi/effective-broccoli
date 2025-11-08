import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:

    if not json_path.lower().endswith('.json'):
        raise ValueError (f"file {json_path} must to be .json")

    if not csv_path.lower().endswith('.csv'):
        raise ValueError (f"file {csv_path} must to be .csv")

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

    if not csv_path.lower().endswith('.csv'):
        raise ValueError (f"file {csv_path} must to be .csv")
        
    if not json_path.lower().endswith('.json'):
        raise ValueError (f"file {json_path} must to be .json")
        
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

        # print("converting people.json to CSV...")
        # json_to_csv("./people1.csv", "data/out/people_from_json.csv")
        # print("the conversion was successful: people_from_json.csv")

        print("converting people.csv to JSON...")
        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print("the conversion was successful: people_from_csv.json")
        
    except Exception as e:
        print(f"wrong: {e}")


if __name__ == "__main__":
    main()