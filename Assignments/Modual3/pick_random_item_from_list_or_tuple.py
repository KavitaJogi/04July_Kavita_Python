import random

mylist=[]

n=int(input("Enter list size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

random_item=random.choice(mylist)
print("Random item is : ",random_item)