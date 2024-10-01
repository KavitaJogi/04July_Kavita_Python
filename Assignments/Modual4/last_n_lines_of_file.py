f = open("demofile.txt", "r")

for i in(f.readlines() [-1:]):
    print(i,end="")
f.close()
