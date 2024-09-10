mydict={}

n=int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    mydict[key]=value

unique_values=set()

for j in mydict.values():
    unique_values.add(j)

print("Unique values in the dictionary : ", unique_values)