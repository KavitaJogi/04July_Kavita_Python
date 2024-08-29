mylist=[]

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

tuple=tuple(mylist)

exist=input("Enter Element from Tuple : ")

if exist in tuple:
        print(f"Element {exist} is within tuple.")
else:
        print(f"Element {exist} is not within tuple.")