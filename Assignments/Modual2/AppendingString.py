mystr=input("Enter String: ")
length=len(mystr)

if length>2:
    if mystr.endswith('ing'):
        mystr+='ly'
    else:
        mystr+='ing'
print("New string: ",mystr)