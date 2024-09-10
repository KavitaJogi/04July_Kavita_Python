tuple1=[]
tuple2=[]

dic={}

print("Enter same Number of element in both tuple")

n1=int(input("Enter size for Tuple1 : "))

for i in range(n1):
    add=input("Enter Element : ")
    tuple1.append(add)

n2=int(input("Enter size for Tuple2 : "))

for j in range(n2):
    add=input("Enter Element : ")
    tuple2.append(add)


tuple1=tuple(tuple1)
tuple2=tuple(tuple2)

length=len(tuple1)

for k in range(length):
    dic[tuple1[k]]=tuple2[k]

print(dic)