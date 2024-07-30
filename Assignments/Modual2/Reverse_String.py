mystr=input("Enter String: ")
length=len(mystr)
if length%4==0:
    r=mystr[::-1]
    print(r)