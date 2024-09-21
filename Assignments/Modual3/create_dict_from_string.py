char_count={}

str=input("Enter a String : ")

for i in str:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)