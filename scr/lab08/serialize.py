import json
from typing import List
from .models import Student

def students_to_json(students: List[Student], path: str):

    # Convert each student to dictionary
    students_data = [student.to_dict() for student in students]
    
    # Write to JSON file
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(students_data, f, ensure_ascii=False, indent=2)
    
    print(f"Saved data of {len(students)} students to {path}")

def students_from_json(path: str) -> List[Student]:

    try:
        with open(path, 'r', encoding='utf-8') as f:
            students_data = json.load(f)
        
        students = []
        for data in students_data:
            try:
                student = Student.from_dict(data)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Warning: Skipping invalid student data - {e}")
                continue
        
        print(f"Loaded {len(students)} students from {path}")
        return students
        
    except FileNotFoundError:
        print(f"Error: File {path} not found")
        return []
    except json.JSONDecodeError:
        print(f"Error: File {path} is not a valid JSON format")
        return []