mylist=[]

n=int(input("Enter list size: "))
for i in range(n):
    add=input("Enter element in list: ")
    mylist.append("\n"+add)

file = open('demofile.txt','a')
for  i in mylist:
	file.write(i+"\n")
file.close()