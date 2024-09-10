mylist=[]
empty_tuple=[]
n=int(input("how many tuple you want to enter : "))

for i in range(n):
    add=input(f"Enter {i+1} element : ")
    mylist.append(tuple(add.split()))

print(f"Original Tuple is : {mylist}")

for j in mylist:
    if j:
        empty_tuple.append(j)

print(f"Remove Empty Tuple From List of Tuple : {empty_tuple}")
