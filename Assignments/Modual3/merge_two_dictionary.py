dict1={}
dict2={}



n1=int(input("Enter Number of Dictionary Pairs for dictionary 1: "))

for i in range(n1):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    dict1[key]=value


n2=int(input("Enter Number of Dictionary Pairs for dictionary 2: "))

for i in range(n2):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    dict2[key]=value

dict1.update(dict2)

print(dict1)