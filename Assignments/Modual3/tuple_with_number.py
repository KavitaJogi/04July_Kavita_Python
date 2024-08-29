my_tuple=[]

n=int(input("Enter tuple size : "))

for i in range(n):
    add=int(input("Enter number in tuple : "))
    my_tuple.append(add)
    
print(tuple(my_tuple))