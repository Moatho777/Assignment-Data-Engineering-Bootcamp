import csv
from models import Student
def load_students_from_csv(file_path):
    students = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    student_id = int(float(row['StudentID']))
                    name = row['Name'].strip()
                    grades_str = row.get('Grades', '').strip()
                    grades = [float(g.strip()) for g in grades_str.split(',') if g.strip()] if grades_str else []
                    student = Student(name, student_id, grades)
                    students.append(student)
                except (ValueError, KeyError) as e:
                    print(f"Skipping invalid row: {e}")
                    continue
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return students

def save_students_to_file(students, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['StudentID', 'Name', 'Grades'])
            for student in students:
                grades_str = ','.join(f"{g:.2f}" for g in student.grades)
                writer.writerow([student.student_id, student.name, grades_str])
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def validate_student_id(student_id):
    try:
        return int(student_id) > 0
    except (ValueError, TypeError):
        return False

def validate_name(name):
    return isinstance(name, str) and len(name.strip()) > 0

def validate_grades(grades_str):
    try:
        grades = [float(g.strip()) for g in grades_str.split(',') if g.strip()]
        return len(grades) > 0
    except ValueError:
        return False