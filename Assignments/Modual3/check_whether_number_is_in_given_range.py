start=int(input("Enter number you want to start range : "))
end=int(input("Enter number you want to end range : "))

num=int(input("Enter Number : "))

if start <= num <= end:
    print(f"{num} is in the range {start} to {end}.")
else:
    print(f"{num} is not in the range {start} to {end}.")