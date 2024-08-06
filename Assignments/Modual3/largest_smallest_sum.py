data=[]
sum=0
n=int(input("Enter list size: "))
for i in range(0,n):
    add=input("Enter element in list: ")
    val=int(add)
    data.append(val)
print(data)

#-----------------------------------lagest_num in list-------------------------------------------------#

print(f"Maximum element is {max(data)}")

#-----------------------------------smallest_num in list----------------------------------------------#

print(f"Minimum element is {min(data)}")

#---------------------------------sum of all number---------------------------------------------------#

for i in range(0,len(data)):
    sum=sum+data[i]
print(f"Sum of all element in list: {sum}")