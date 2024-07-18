num1=0
num2=1
count=0
ntime=int(input("Enter number you want to print for fibonacci series: "))
print("Fibonacci sequence is: ")
while count<ntime:
    print(num1)
    n=num1+num2
    num1=num2
    num2=n
    count+=1