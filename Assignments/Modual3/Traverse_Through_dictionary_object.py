mydict={}

n=int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    mydict[key]=value

for i,j in mydict.items():
    print(f"\nkey : {i} , value : {j}")