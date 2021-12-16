class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = float()

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def count_average(self):
        sum_grades = int()
        len_grades = int()
        for hw_grades in self.grades.values():
            for hw_sum in hw_grades:
                sum_grades += hw_sum
            len_grades += len(hw_grades)
        self.average = round((sum_grades / len_grades), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.average < other.average

    def __str__(self):
        self.courses_in_progress_str = ','.join(self.courses_in_progress)
        self.finished_courses_str = ','.join(self.finished_courses)
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка задомашнее задание:{self.average} \n' \
              f'Курсы в процессе обучения: {self.courses_in_progress_str} \n' \
              f'Завершенные курсы: {self.finished_courses_str}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.lec_grades = {}
        self.average = float()

    def count_average(self):
        sum_grades = int()
        len_grades = int()
        for course_grades in self.lec_grades.values():
            for course_sum in course_grades:
                sum_grades += course_sum
            len_grades += len(course_grades)
        self.average = round((sum_grades / len_grades),  1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.average < other.average

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname} \n' \
              f'Средняя оценка за курсы:{self.average}'
        return res


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n' \
              f'Фамилия: {self.surname}'
        return res


some_reviewer1 = Reviewer('Kory', 'Brown')
some_reviewer1.courses_attached = ['Python']

some_reviewer2 = Reviewer('Nick', 'Buddy')
some_reviewer2.courses_attached = ['Literature']


some_lecturer1 = Lecturer('Mike', 'Oldman')
some_lecturer1.courses += ['literature']
some_lecturer1.courses += ['Git']
some_lecturer1.lec_grades['literature'] = [6, 8, 5, 9]
some_lecturer1.lec_grades['Git'] = [2, 6]

some_lecturer2 = Lecturer('Kelly', 'Miles')
some_lecturer2.courses += ['Python']
some_lecturer2.courses += ['Math']
some_lecturer2.lec_grades['Python'] = [3, 4]
some_lecturer2.lec_grades['Math'] = [6, 8, 5]

some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student1.finished_courses += ['Git']
some_student1.courses_in_progress += ['Math']
some_student1.grades['Git'] = [10, 4, 10, 7, 10]
some_student1.grades['Math'] = [8, 10]

some_student2 = Student('Dilan', 'Fry', 'your_gender')
some_student2.finished_courses += ['Git']
some_student2.courses_in_progress += ['Python']
some_student2.grades['Git'] = [1, 4, 3, 8, 10]
some_student2.grades['Python'] = [10, 10]

some_student1.count_average()
print(some_student1)
print()
print(some_reviewer1)
print()
some_lecturer1.count_average()
print(some_lecturer1)
print(some_student1 < some_student2)
print()


student_list = [{"name": "Ruoy Eman", "Git": [10, 4, 10, 7, 10], "Math": [8, 10]},
                {"name": "Dilan Fry", "Git": [1, 4, 3, 8, 10], "Python": [10, 10]}]
lecturer_list = [{"name": "Mike Oldman", "literature": [6, 8, 5, 9], "Git": [2, 6]},
                {"name": "Kelly Miles", "Python": [3, 4], "Math": [6, 8, 5]}]
course_name = "Git"


def count_course_hw_average(student_list, course_name):
    course_grades = int()
    numbers_grades = int()
    for student in student_list:
        if course_name in student.keys():
            for grade in student[course_name]:
                course_grades += grade
            numbers_grades += len(student[course_name])
    course_average = course_grades / numbers_grades
    print(course_average)


def count_course_lecturer_average(lecturer_list, course_name):
    course_grades = int()
    numbers_grades = int()
    for lecturer in lecturer_list:
        if course_name in lecturer.keys():
            for grade in lecturer[course_name]:
                course_grades += grade
                numbers_grades += len(lecturer[course_name])
    course_lecturer_average = course_grades / numbers_grades
    print(course_lecturer_average)


count_course_hw_average(student_list, course_name)
count_course_lecturer_average(lecturer_list, course_name)

