mylist=[]
temp=[]
n=int(input("Enter list size:"))
for i in range(n):
    add=input("Enter value in list: ")
    mylist.append(add)
    for i in mylist:
        temp=list(set(mylist))
print(temp)