count=0
str=input("Enter Any String: ")
substr=input("Enter Any Substring: ")
if substr in str:
    count=str.count(substr)
print("The Substring count is: ",count)
