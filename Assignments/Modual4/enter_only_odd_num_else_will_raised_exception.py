try:
    num=int(input("Enter Number : "))
    if num % 2 != 0:
        print(f"{num} is Odd.")
    else:
        raise ValueError("Not an odd number")
except Exception as e:
    print(e)
