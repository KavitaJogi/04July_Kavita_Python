data=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    st_name=input("Enter student name: ")
    data.append(st_name)
print(tuple(data))
