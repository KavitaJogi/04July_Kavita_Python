mylist=[]
string=""
n=int(input("Enter list size: "))
for i in range(n):
    add=input("Enter character in list: ")
    mylist.append(add)
for j in mylist:
    string=string+j
print(string)