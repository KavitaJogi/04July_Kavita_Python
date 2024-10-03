f=open("demofile.txt",'r')

max_len=0
l_word=""

for i in f:
    word=i.strip().split()

    for j in word:
        if len(j)>max_len:
            max_len=len(j)
            l_word=j

        elif len(j)==max_len:
            l_word+=" "+j
print("Longest word : ",l_word)