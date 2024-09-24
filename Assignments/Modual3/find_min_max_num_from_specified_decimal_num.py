mylist=[]

num= int(input("Enter size : "))

for i in range(num):
    add=float(input("Enter Decimal Number : "))
    mylist.append(add)

max_num = max(mylist)
min_num = min(mylist)

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")