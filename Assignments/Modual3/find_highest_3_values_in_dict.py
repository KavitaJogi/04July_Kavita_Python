mydict={}
list=[]

n=int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    list.append(value)
    mydict[key]=value


for j in range(3):  
    n=max(list)
    print(f"Highest {j+1} values are : ",n)
    list.remove(n)


