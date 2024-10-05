class Person:
    def setData(self, name):
        self.name = name
        print("Name:", self.name)

class Student(Person):
    def setStudentID(self, student_id):
        self.student_id = student_id
        print("Student ID:", self.student_id)

student = Student()

name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")

student.setData(name)
student.setStudentID(student_id)