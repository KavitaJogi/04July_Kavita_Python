mylist=[]
temp=[]
repeated_element=[]

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

for i in mylist:
    if i not in temp:
        temp.append(i)
    else:
        repeated_element.append(i)

print("Repeted item of tuple is : ",tuple(repeated_element))
