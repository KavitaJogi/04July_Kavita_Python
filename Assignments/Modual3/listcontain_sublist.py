mainlist=[]
sublist=[]

n1=int(input("Enter list size for main list : "))
n2=int(input("Enter list size for sun list : "))

for i in range(n1):
    add=input("Enter element in list: ")
    mainlist.append(add)

for j in range(n2):
    sub=input("Enter element in sublist: ")
    sublist.append(sub)

set_mainlist=set(mainlist)
set_sublist=set(sublist)

if(set_mainlist.intersection(set_sublist)):
    print("List contains a Sub List")
else:
    print("List not contain a Sub List")