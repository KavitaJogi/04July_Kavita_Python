mystr=input("Enter String: ")
length=len(mystr)
print(mystr)

if length>=2 and mystr.startswith("a") and mystr.endswith("a"):
    print(mystr)
else:
    print("error")
