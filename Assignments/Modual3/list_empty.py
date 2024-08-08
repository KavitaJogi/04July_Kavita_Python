mylist=[]
n=int(input("Enter a list size: "))
for i in range(n):
    add=input("Enter value in list: ")
    mylist.append(add)
    length=len(mylist)
    if length!=1:
        print("List is empty")
    else:
        print("List is not empty")
