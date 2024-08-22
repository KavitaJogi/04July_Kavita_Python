str=[]
count=0
n=int(input("Enter number of string:"))
for i in range(n):
    mystr=input("Enter String: ")
    str.append(mystr)
print(str)
length=len(str)
for i in str:    
    if length>=2 and i[0] == i[-1]:
        count+=1
print(f"Matching Strings are: {count}")
