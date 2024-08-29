mylist=[]

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

tuple=tuple(mylist)

print(f"\nTuple is : {tuple}")
