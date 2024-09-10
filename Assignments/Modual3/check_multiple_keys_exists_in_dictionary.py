mydict={}
key_check=[]

n=int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    mydict[key]=value

print(mydict)

check=int(input("Enter number of check keys : "))

for j in range(check):
    add=input(f"Enter {j+1} key : ")
    key_check.append(add)

for k in key_check:
    if k in mydict:
        print(f"{k} exists in a dictionary.")    
    else:
        print(f"{k} does not exists in a dictionary.")