from models import Student, Classroom
from analytics import top_performing_student, lowest_performing_student, ranking_students, grade_distribution
from utils import load_students_from_csv, save_students_to_file, validate_student_id, validate_name, validate_grades
import os

def main():
    classroom = Classroom()
    data_file = 'data.csv'

    # Load existing data
    if os.path.exists(data_file):
        students = load_students_from_csv(data_file)
        for student in students:
            try:
                classroom.add_student(student)
            except ValueError as e:
                print(f"Error adding student: {e}")
        print(f"Loaded {len(students)} students from {data_file}")
    else:
        print("No data file found, starting with empty classroom.")

    while True:
        print("\n" + "="*40)
        print("Student Performance Analyzer System")
        print("="*40)
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Show Classroom Average")
        print("5. Show Top Performing Student")
        print("6. Show Lowest Performing Student")
        print("7. Show Student Rankings")
        print("8. Show Grade Distribution")
        print("9. Save Data")
        print("10. Exit")
        print("-"*40)

        try:
            choice = input("Enter your choice (1-10): ").strip()
        except KeyboardInterrupt:
            print("\nExiting...")
            break

        if choice == '1':
            try:
                name = input("Enter student name: ").strip()
                if not validate_name(name):
                    print("Invalid name. Please enter a non-empty string.")
                    continue

                student_id_str = input("Enter student ID (positive integer): ").strip()
                if not validate_student_id(student_id_str):
                    print("Invalid student ID. Please enter a positive integer.")
                    continue
                student_id = int(student_id_str)

                if classroom.search_student(student_id):
                    print("Student ID already exists.")
                    continue

                grades_str = input("Enter grades separated by commas (e.g., 85.5,90.0): ").strip()
                if not validate_grades(grades_str):
                    print("Invalid grades. Please enter numbers separated by commas.")
                    continue

                grades = [float(g.strip()) for g in grades_str.split(',') if g.strip()]
                student = Student(name, student_id, grades)
                classroom.add_student(student)
                print("Student added successfully.")
            except Exception as e:
                print(f"Error adding student: {e}")

        elif choice == '2':
            try:
                student_id_str = input("Enter student ID to remove: ").strip()
                if not validate_student_id(student_id_str):
                    print("Invalid student ID.")
                    continue
                student_id = int(student_id_str)
                classroom.remove_student(student_id)
                print("Student removed (if existed).")
            except Exception as e:
                print(f"Error removing student: {e}")

        elif choice == '3':
            try:
                student_id_str = input("Enter student ID to search: ").strip()
                if not validate_student_id(student_id_str):
                    print("Invalid student ID.")
                    continue
                student_id = int(student_id_str)
                student = classroom.search_student(student_id)
                if student:
                    print(f"Found: Name: {student.name}, ID: {student.student_id}, "
                          f"Average: {student.calculate_average():.2f}, Category: {student.determine_grade_category()}")
                else:
                    print("Student not found.")
            except Exception as e:
                print(f"Error searching student: {e}")

        elif choice == '4':
            avg = classroom.calculate_classroom_average()
            print(f"Classroom Average: {avg:.2f}")

        elif choice == '5':
            # Show Top Performing Student
            top = top_performing_student(classroom)
            if top:
                print(f"Top Performing: {top.name} (ID: {top.student_id}), Average: {top.calculate_average():.2f}")
            else:
                print("No students in classroom.")

        elif choice == '6':
            # Show Lowest Performing Student
            low = lowest_performing_student(classroom)
            if low:
                print(f"Lowest Performing: {low.name} (ID: {low.student_id}), Average: {low.calculate_average():.2f}")
            else:
                print("No students in classroom.")

        elif choice == '7':
            rankings = ranking_students(classroom)
            if rankings:
                print("Student Rankings (by average grade, descending):")
                for i, student in enumerate(rankings, 1):
                    print(f"{i}. {student.name} (ID: {student.student_id}): {student.calculate_average():.2f}")
            else:
                print("No students in classroom.")

        elif choice == '8':
            # Show Grade Distribution
            dist = grade_distribution(classroom)
            print("Grade Distribution:")
            for cat, count in dist.items():
                print(f"  {cat}: {count} students")

        elif choice == '9':
            # Save Data
            save_students_to_file(classroom.students, data_file)

        elif choice == '10':
            # Exit
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
