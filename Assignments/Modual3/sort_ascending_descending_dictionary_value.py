mydict={}

n=int(input("Enter Number of Dictionary Pairs: "))

for i in range(n):
    key=input(f"Enter {i+1} key : ")
    value=input(f"Enter {i+1} value : ")
    mydict[key]=value

ascending=sorted(mydict.values())

print("Value sorted in ascending order :",ascending)

descending=sorted(mydict.values(),reverse=True)

print("Value sorted in descending order :",descending)