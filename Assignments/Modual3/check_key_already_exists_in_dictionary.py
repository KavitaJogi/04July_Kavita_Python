mydict={}

n=int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    mydict[key]=value

check=input("Enter Key Name : ")

if check in mydict:
    print(f"Key '{check}' is already exists.")
else:
    print(f"Key '{check}' is not exists.")