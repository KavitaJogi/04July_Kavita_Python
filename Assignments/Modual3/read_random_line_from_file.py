import random
#fl=open('stdata.txt','w')

lines = open('stdata.txt').read().splitlines()
x=random.choice(lines)

print(x)