sum = 0
num=int(input("Enter number : "))

if num <= 0:
    print("Please enter positive number.")
else:
    for x in range(1, num): 
        if num % x == 0:
            sum += x
    if sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
