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