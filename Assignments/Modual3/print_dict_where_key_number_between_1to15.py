mydict = {} 

n=int(input("Enter Number of Dictionary Pairs : "))

if n<=15:
    for i in range(n):
        key1 = input(f"Enter {i+1} Keys : ")    #get value
        value1 = input(f"Enter {i+1} Values : ")
        mydict[key1] = value1    #add key and value in dict1
    print(mydict)
else:
    print("Please! Enter number between 1 and 15.")