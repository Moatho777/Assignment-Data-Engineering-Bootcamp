class Student:
    def __init__(self, name, student_id, grades):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades

    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def grades(self):
        return self.__grades.copy()

    def calculate_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    def determine_grade_category(self):
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    @classmethod
    def from_dict(cls, data):
        grades = [data.get('FinalGrade', 0)]
        return cls(data['Name'], int(data['StudentID']), grades)

    def __str__(self):
        return f"Student({self.__name}, {self.__student_id}, {self.__grades})"


class Classroom:
    def __init__(self):
        self.__students = []

    @property
    def students(self):
        return self.__students.copy()

    def add_student(self, student):
        if not isinstance(student, Student):
            raise ValueError("Must be a Student instance")
        self.__students.append(student)

    def remove_student(self, student_id):
        self.__students = [s for s in self.__students if s.student_id != student_id]

    def search_student(self, student_id):
        for student in self.__students:
            if student.student_id == student_id:
                return student
        return None

    def calculate_classroom_average(self):
        if not self.__students:
            return 0.0
        return sum(s.calculate_average() for s in self.__students) / len(self.__students)

    @staticmethod
    def sort_students_by_average(students):
        return sorted(students, key=lambda s: s.calculate_average(), reverse=True)