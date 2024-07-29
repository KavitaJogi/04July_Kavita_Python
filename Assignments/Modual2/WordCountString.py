count=0
a=[]
sentence=input("Enter Any Sentence: ")
word=input("Enter Word:")
a=sentence.split(" ")
for i in range(0,len(a)):
    if word==a[i]:
        count=count+1
print(f"Occurance of word is {count}")