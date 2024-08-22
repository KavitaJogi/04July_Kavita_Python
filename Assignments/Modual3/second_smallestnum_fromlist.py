mylist=[]
n=int(input("Enter list size: "))
for i in range(n):
    add=input("Enter Item in list: ")
    val=int(add)
    mylist.append(val)
mylist.sort()
print(mylist)
print(f"Second smallest number is {mylist[1]}")


