"""
--> First try clause is executed i.e. the code between try and except clause.
--> If there is no exception, then only try clause will run, except clause will not get executed.
--> If any exception occurs, the try clause will be skipped and except clause will run.
--> If any exception occurs, but the except clause within the code doesn’t handle it, it is passed on to the outer try statements. 
--> If the exception is left unhandled, then the execution stops.
--> A try statement can have more than one except clause.
--> The finally block always executes after normal termination of try block or after try block terminates due to some exception.
--> Even if you return in the except block still the finally block will execute.
"""

#example:

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
        
