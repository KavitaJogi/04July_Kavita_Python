class StudInfo:
    def __init__(self, id, name, subject): 
        self.id = id
        self.name = name
        self.subject = subject

class StudData(StudInfo): 
    def studData(self):
        print("Id : ",self.id)
        print("Name : ",self.name)
        print("Subject : ",self.subject)

id = int(input("Enter Student id : "))
name = input("Enter Student Name : ")
subject = input("Enter Student Subject : ")

stud = StudData(id, name, subject)
stud.studData()