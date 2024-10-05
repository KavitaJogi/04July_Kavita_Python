class Faculty:
    def getData(self, faculty_name):
        self.faculty_name = faculty_name
        print("Faculty Name:", self.faculty_name)

class Course(Faculty):
    def getCourse(self, course_name):
        self.course_name = course_name
        print("Course Name:", self.course_name)

c1 = Course()

fname = input("Enter Faculty Name : ")
cname = input("Enter Course Name : ")

c1.getData(fname)
c1.getCourse(cname)
