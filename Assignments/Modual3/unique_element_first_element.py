mylist=[]
unique_list=[]
n=int(input("Enter list size: "))
for i in range(n):
    add=int(input("Enter value in list: "))
    mylist.append(add)
for j in mylist:
    if j not in unique_list:
        unique_list.append(j)
print(unique_list)