mylist=[]

n=int(input("how many tuple you want to enter : "))

for i in range(n):
    add=input(f"Enter {i+1} two Element by comma sepreted : ")
    mylist.append(add.split(","))
    tuple(mylist)

print(f"\nList of tuple : {mylist}\n")

if n>=2:
    print(dict(mylist))
