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