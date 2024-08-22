mylist=[]
n=int(input("Enter list size: "))
for i in range(0,n):
    add=input("Enter element in list: ")
    mylist.append(add)
uniq_val=set(mylist)
print(f"Unique Elements are: {list(uniq_val)}")