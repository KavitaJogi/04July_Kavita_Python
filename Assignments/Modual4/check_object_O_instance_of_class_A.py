class A:
    print("This is class A.")

o = A()

if isinstance(o, A):
    print("o is an instance of class A")
else:
    print("o is not an instance of class A")