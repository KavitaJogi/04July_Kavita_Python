mylist=[]

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

print(mylist)

replace=input("Enter element to replace into last index : ")
mylist[-1]=replace

tuple=tuple(mylist)

print(f"After replace tuple is : {tuple}")