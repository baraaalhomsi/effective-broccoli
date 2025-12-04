# ЛР8 – ООП в Python: @dataclass Student, методы и сериализация

## A. Реализовать класс Student (models.py)

```python
from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):

        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date format must be YYYY-MM-DD")

        if not (0 <= self.gpa <= 10):
            raise ValueError("GPA must be between 0 and 10")
    
    def age(self) -> int:

        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        #Calculate age considering if birthday has occurred this year
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age
    
    def to_dict(self) -> dict:

        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict):

        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self) -> str:
   
        return f"Student(fio='{self.fio}', group='{self.group}', gpa={self.gpa}, age={self.age()})"
    
    def __repr__(self) -> str:

        return f"Student(fio='{self.fio}', birthdate='{self.birthdate}', group='{self.group}', gpa={self.gpa})"
```

## B. Реализовать модуль serialize.py

```python
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
```
## main.py

```python
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from models import Student
    from lab08.serialize import students_to_json, students_from_json
except ImportError:
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    from models import Student
    from lab08.serialize import students_to_json, students_from_json

def main():
    print("=== Lab 8 Test ===")

    students = [
        Student("Baraa Osaid Alhomsi", "2002-05-15", "SE-01", 8.5),
        Student("Ahmed Mohammed Al Ali", "2003-08-22", "CS-02", 9.2),
        Student("Fatima Abdullah", "2001-12-03", "IT-01", 7.8)
    ]
    
    print("\n=== Student Data ===")
    for student in students:
        print(student)
        print(f"  Age: {student.age()} years")

    os.makedirs("data/lab08", exist_ok=True)

    print("\n=== Serialization Test ===")
    output_path = "data/lab08/students_output.json"
    students_to_json(students, output_path)

    print("\n=== Deserialization Test ===")
    loaded_students = students_from_json(output_path)
    
    print("\n=== Loaded Students ===")
    for student in loaded_students:
        print(student)
    
    # Test validation
    print("\n=== Validation Test ===")
    try:
        invalid_student = Student("Mohammed", "2023-13-45", "SE-01", 8.5)
    except ValueError as e:
        print(f"Expected date error: {e}")
    
    try:
        invalid_student = Student("Mohammed", "2023-01-01", "SE-01", 15.0)
    except ValueError as e:
        print(f"Expected GPA error: {e}")
    
    print("\n=== Test Completed Successfully! ===")

if __name__ == "__main__":
    main()
```

## students_input.json

![alt text](/images/lab08/Screenshot%202025-11-29%20123705.png)

## into the terminal "python scr/lab08/main.py"

![alt text](/images/lab08/Screenshot%202025-11-29%20123547.png)

## students_output.json

![alt text](/images/lab08/Screenshot%202025-11-29%20123756.png)