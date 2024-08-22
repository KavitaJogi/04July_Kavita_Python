import random
mylist=[]
n=int(input("Enter list size: "))
for i in range(n):
    add=input("Enter Item in list: ")
    mylist.append(add)
print(mylist)
random=random.choice(mylist)
print(random)