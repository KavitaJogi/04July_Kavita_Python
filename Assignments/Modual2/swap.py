#with temp variable
print("______With Temp Variable____________")
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

num3=num1
num1=num2
num2=num3
print("Swap Numbers: ",num1,num2)

#without temp variable
print("______Without Temp Variable____________")
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("Swap Numbers: ",num1,num2)