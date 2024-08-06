def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n=int(input("Enter Number of student: "))
for i in range(n):
    id=input("Enter ID: ")
    name=input("Enter name:")
    city=input("Enter city: ")
    getdata(id,name,city)
