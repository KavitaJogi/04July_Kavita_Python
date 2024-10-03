f = open("demofile.txt","r")
str=""

for i in range(0,100):
    str=str + f.read(i)

print(str)
