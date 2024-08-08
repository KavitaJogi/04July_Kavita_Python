mylist1=[]
mylist2=[]

n1=int(input("Enter size for list1: "))

for i in range(n1):
    add=input("Enter value in list1: ")
    mylist1.append(add)
print(mylist1)

n2=int(input("Enter size for list2: "))

for j in range(n2):
    add=input("Enter value in list2: ")
    mylist2.append(add)
print(mylist2)

set1=set(mylist1)
set2=set(mylist2)

if set1.intersection(set2):
    print("One common member is in both of list")
else:
    print("No common member found in both of list")

