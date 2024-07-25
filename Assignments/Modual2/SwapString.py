str1=input("Enter first String: ")
str2=input("Enter second String: ")

print(str1+" "+str2)

swapstr1= str2[:2]+str1[2:]
swapstr2=str1[:2]+str2[2:]
newstr=swapstr1+" "+swapstr2

print("Swaping character of string: ",newstr)