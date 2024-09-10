list1_key=[]
list2_value=[]

key=int(input("Enter Number of Keys : "))

for i in range(key):
    add=input(f"Enter {i+1} key in list1: ")
    list1_key.append(add)

value=int(input("Enter Number of Values : "))

for j in range(value):
    add=input(f"Enter {j+1} key in list2: ")
    list2_value.append(add)

length_key=len(list1_key)
length_value=len(list2_value)

if length_key!= length_value:
    print("Both lists must have the same length.")
else:
    print(dict(zip(list1_key, list2_value)))