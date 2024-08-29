mylist=[]
string=""

n=int(input("Enter size : "))

for i in range(n):
    add=input("Enter element : ")
    mylist.append(add)

tuple=tuple(mylist)
print(tuple)

for i in tuple:
    string=string+i

print(f"The String is : {string}")