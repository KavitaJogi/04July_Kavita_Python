mylist = [(1, 'hello'), (2, 'this'), (3, 'is'),(4, 'python')]     

list1 = []
list2 = []

for i in mylist:
    list1.append(i[0])    
    list2.append(i[1])   

print("First elements:", list1) 
print("Second elements:", list2)