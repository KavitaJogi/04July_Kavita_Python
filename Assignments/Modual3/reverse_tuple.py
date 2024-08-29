mylist=[]

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

mylist.reverse()
rev_tuple=tuple(mylist)

print(f"\nReverse Tuple is : {rev_tuple}")
