class Person :
    def __init__(self, fullname, age, is_married = 'Unknown'):
        self.fullname = fullname
        self.age = age
        self.married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname}, Age: {self.age}, Married: {self.married}')


class Student(Person):
    def __init__(self, fullname, age, marks, is_married='Unknown'):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def gpa (self):
        return round((sum(self.marks.values())) / len(self.marks), 2)

class Teacher(Person):
    base_salary = 25_000

    def __init__(self, fullname, age, experience, is_married='Unknown'):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def bonus_salary(self):
        base = self.base_salary
        stop = self.experience - 3

        while stop > 0:
            bonus = base * 0.05
            base += bonus
            stop -= 1
        return round(base, 1)

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Experience: {self.experience} years')


teacher = Teacher("Bekmuratov Adil ", 35, 9, 'No')
teacher.introduce_myself()
print(f'Salary: {teacher.bonus_salary()} som\n')

def create_students():
    student_1 = Student('Adilet', 18, marks={'Math': 5, 'History': 3, 'English': 5, 'Biology': 3})
    student_2 = Student('Din Winchester', 44, is_married= 'Yes', marks={'Math': 3, 'History': 4, 'English': 5, 'Biology': 3})
    student_3 = Student('Ana De Armas', 35, is_married= 'Yes', marks={'Math': 4, 'History': 3, 'English': 5, 'Biology': 5})
    list_student = [ student_1, student_2, student_3 ]
    return list_student


students = create_students()

for student in students:
    student.introduce_myself()
    print(f'Marks student:')
    for subject, mark in student.marks.items():
        print(f'{subject} - {mark}')
    print(f'GPA: {student.gpa()}\n')
