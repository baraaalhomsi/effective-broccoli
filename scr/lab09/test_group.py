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