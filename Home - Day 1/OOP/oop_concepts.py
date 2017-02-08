# real-world problem modeled using OOP
# Depicts inheritance, encapsulation, polymorphism and the other OOP concepts.


class Person:

    def __init__(self, name, surname, id_number, student_type):
        self.name = name
        self.surname = surname
        self.id_number = id_number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)

    def courses_taught(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)

alex = Student(Student.POSTGRADUATE, "Alex", "Ngugi", "BIT-035-145/2012")
