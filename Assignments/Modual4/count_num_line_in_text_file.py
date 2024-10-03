file_name= "demofile.txt"

f=open(file_name,'r')

line=len(f.readlines())

print(f"Lines in {file_name} are : {line}")