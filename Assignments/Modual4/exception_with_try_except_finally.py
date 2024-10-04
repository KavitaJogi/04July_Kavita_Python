x = int(input("Enter first number : "))     
y = int(input("Enter second number :"))

try:
    sum = x + y
    sub = x - y
    mult = x * y
    div = x / y
    print("Addition : ",sum)
    print("Subtraction : ",sub)
    print("Multiplication : ",mult)
    print("Division : ",div)
except Exception as e:
    print(e)
finally:
    print("This is always executed")
        
