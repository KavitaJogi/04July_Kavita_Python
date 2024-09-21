list = []

n = int(input("Enter Number of Dictionary Pairs : "))

for i in range(n):
    item=input(f"Enter {i+1} key : ")
    amount=input(f"Enter {i+1} value : ")
    list.append({'item' : item, 'amount' : amount})

mydict = {} 

for i in list:
    item = i['item']
    amount = i['amount']
    if item in mydict:
        mydict[i['item']] += i['amount']
    else:
        mydict[i['item']] = i['amount']

print(mydict)