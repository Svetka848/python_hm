class СomparedObject:

    def get_average_grade(self):
        pass

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()


class Student(СomparedObject):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {self.get_average_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def get_average_grade(self):
        grade_list = []
        for course in self.grades.values():
            grade_list += course

        if len(grade_list) > 0:
            return sum(grade_list) / len(grade_list)
        else:
            return '-'

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def finish_course(self, course):
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
            self.finished_courses.append(course)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor, СomparedObject):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.get_average_grade()}\n'

    def get_average_grade(self):
        grade_list = []
        for course in self.grades.keys():
            for student in self.grades[course].keys():
                grade_list.append(self.grades[course][student])

        if len(grade_list) > 0:
            return sum(grade_list) / len(grade_list)
        else:
            return '-'

    def grade_student(self, course, student, grade):
        if (isinstance(student, Student)) and (course in self.courses_attached) and (
                course in student.courses_in_progress):
            if course not in self.grades.keys():
                self.grades[course] = {}
            self.grades[course][student] = grade

        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def get_average_hm_grade_by_course(students, course):
    grades = []
    for student in students:
        student_grades = student.grades
        if course in student_grades.keys():
            for grade in student_grades[course]:
                grades.append(grade)
    return sum(grades) / len(grades)


def get_average_lecture_grade_by_course(lectures, course):
    grades = []
    for lecture in lectures:
        lecture_grades = lecture.grades
        if course in lecture_grades.keys():
            for student in lecture_grades[course]:
                grades.append(lecture_grades[course][student])
    return sum(grades) / len(grades)
