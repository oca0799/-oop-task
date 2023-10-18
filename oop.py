

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        rate = 0
        amount = 0
        for bin in self.grades.values():
            rate += sum(bin)
            amount += len(bin)
        return round(rate / amount, 1)

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating()}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.courses_attached = courses_attached
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}


    def average_rating(self):
        averages_ratings = list(self.grades.values())
        rate = 0
        amount = 0
        for bin in averages_ratings:
            rate += sum(bin)
            amount += len(bin)
        if amount == 0:
            return 'Нет оценок'
        return round(rate / amount, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.average_rating()}'

    def __lt__(self, other):
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}' + '\n' + f'Фамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

bad_student = Student('Maxim', 'Petrov', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Java']

cool_mentor = Mentor('Some', 'Buddy', [])
cool_mentor.courses_attached += ['Python']

mentor1 = Mentor('Roman', 'Duk', [])
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['Java']


cool_lecturer = Lecturer('Ivan', 'Popov', [])
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']
cool_lecturer.courses_attached += ['Git']

bad_lecturer = Lecturer('Mark', 'Tven', [])
bad_lecturer.courses_attached += ['Java']
bad_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy', [])
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

main_reviewer = Reviewer('Jay', 'Z', [])
main_reviewer.courses_attached += ['Python']
main_reviewer.courses_attached += ['Java']
main_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)

cool_reviewer.rate_hw(bad_student, 'Python', 4)

best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Git', 8)
best_student.rate_hw(cool_lecturer, 'Python', 7)
best_student.rate_hw(cool_lecturer, 'Git', 9)
best_student.rate_hw(cool_lecturer, 'Python', 4)

best_student.rate_hw(bad_lecturer, 'Python', 8)
best_student.rate_hw(bad_lecturer, 'Git', 7)

students_list = [best_student, bad_student]
lecturers_list = [cool_lecturer, bad_lecturer]
def student_average_rating(students_list, course):
    rating = []
    if students_list:
        for student in students_list:
            for key, value in student.grades.items():
                if key == course:
                    rating += value
        return round(sum(rating) / len(rating), 1)

def lecturers_average_rating(lecturers_list, course):
    rating = []
    if lecturers_list:
        for lecturer in lecturers_list:
            for key, value in lecturer.grades.items():
                if key == course:
                    rating += value
        return round(sum(rating) / len(rating), 1)

print(student_average_rating(students_list, 'Python'))
print(lecturers_average_rating(lecturers_list, 'Python'))
print(best_student.grades)
print(bad_student.grades)
print(cool_lecturer.courses_attached)
print(cool_lecturer.courses_attached)
print(cool_lecturer.grades)
print(cool_reviewer)
print(cool_lecturer)
print(bad_lecturer)
print(cool_lecturer.grades)
print(best_student)
print(best_student < best_student)
print(bad_lecturer < cool_lecturer)