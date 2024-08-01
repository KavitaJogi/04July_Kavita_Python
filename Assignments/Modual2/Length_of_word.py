n=int(input("How many word you want to enter? "))
ip_no=[]
for i in range(n):
    word=input("Enter Word: ")
    ip_no.append(word)
maxlen=len(ip_no[0])
temp=ip_no[0]
for j in ip_no:
    if len(j) > maxlen:
        maxlen=len(j)
        temp=j
print(f"word {temp} with the longest length is: {maxlen}")    