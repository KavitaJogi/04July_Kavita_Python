import random
mylist=[]

n=int(input("Enter list size : "))

for i in range(n):
    add=int(input("Enter Item in list : "))
    mylist.append(add)
print(mylist)

random.shuffle(mylist)

print("Randomized Item of list in place is : ",mylist)