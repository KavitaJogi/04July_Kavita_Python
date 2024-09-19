mydict={'1': ['a','b'], '2': ['c','d']}

mylist= list(mydict.values())
for i in mylist[0]:
    for j in mylist[1]:
        print(i+j)