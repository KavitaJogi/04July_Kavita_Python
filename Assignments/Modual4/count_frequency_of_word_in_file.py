f=open("demofile.txt",'r')
d={}
for i in f:
    word=i.strip().split()

    for j in word:
        if j in d:
            d[j]+=1
        else:
            d[j]=1

for k in list(d.keys()):
    print(k,":",d[k])
