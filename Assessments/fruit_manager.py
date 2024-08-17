import Fruit_Market
operation={'1)':'Add Fruit Stock','2)':'View Fruit Stock','3)':'Update Fruit Stock'}
x={}
     
def add():
    print("\nADD FRUIT STOCK")
    name=input("Enter fruit Name: ")
    qty=int(input("Enter qty (in kg): "))
    price=int(input("Enter price: "))
    x[name]={"Qty":qty,"Price":price}

                
def update():
     print("\nUPDATE FRUIT STOCK")
     name=input("Enter fruit Name: ")
     qty=int(input("Enter qty (in kg): "))
     price=int(input("Enter price: "))

     if x[name] in x.keys():
          x[name]={"Qty":qty,"Price":price}
     else:
          x[name]={"Qty":qty,"Price":price}

#-------------------------------- Manager Section-------------------------------#

role=int(input("\nSelect Your Role: "))
print("\nFruit Market Manager")
if role==1:
    for i,j in operation.items():
        print(f"{i}{j}")
        

    choice=int(input("Enter your choice: "))
    if choice==1:
        add()
    if choice==2:
        print("VIEW FRUIT STOCK")
        print({x})
    if choice==3:
        update()

    while True:
          
        more_ope=input("Do you want to perform more operation : press y for yes and n for no : ")
                
        if more_ope=='y':
            choice=int(input("Enter your choice: "))
            if choice==1:
                add()
            if choice==2:
                print("VIEW FRUIT STOCK")
                print({x})
            if choice==3:
                update()


