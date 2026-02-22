from models import Classroom

def top_performing_student(classroom):
    students = classroom.students
    if not students:
        return None
    return max(students, key=lambda s: s.calculate_average())

def lowest_performing_student(classroom):
    students = classroom.students
    if not students:
        return None
    return min(students, key=lambda s: s.calculate_average())

def ranking_students(classroom):
    students = classroom.students
    return Classroom.sort_students_by_average(students)

def grade_distribution(classroom):
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for student in classroom.students:
        cat = student.determine_grade_category()
        dist[cat] += 1
    return dist