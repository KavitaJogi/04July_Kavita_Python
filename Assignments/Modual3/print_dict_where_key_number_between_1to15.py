mydict = {} 

n=int(input("Enter Number of Dictionary Pairs : "))

if n<=15:
    for i in range(n):
        key = input(f"Enter {i+1} key : ")
        value = input(f"Enter {i+1} value : ")
        mydict[key] = value
    print(mydict)

else:
    print("Please enter number between 1 and 15.")