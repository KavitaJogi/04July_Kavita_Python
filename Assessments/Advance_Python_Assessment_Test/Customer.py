customer={}
    
class Customer:
    accno=int(input("enter account number:"))
    customer['accno']=accno
    bal=int(input("enter balance:"))
    customer['bal']=bal

    def register(self):
            self.username = input("Enter username: ")
            self.password = input("Enter password: ")
                            
            customer['Username'] = self.username
            if self.username in customer:
                    print("Customer already exists.")
            else:
                customer['Password']=self.password
                print("Register Successfully")
                print(customer)
    

    def login(self):
        self.username = input("Enter username: ")
        if self.username in customer["Username"]:
            self.password = input("Enter password: ")
            if customer['Password'] == self.password:
                    print("Log in successfully.")
            else:
                    print("Invalid password.")
        else:
            print("Invalid username.")
        print(customer)
    
    
    def withdraw(self):
        self.withdraw=int(input("Enter Amount  you want to Withdraw:"))     
        if self.withdraw<=customer['bal']:
            self.customer_balance=customer['bal']-self.withdraw
            print("Withdraw sucessfully")
            print("your current balance is:",self.customer_balance)
            customer['bal']=self.customer_balance
        else:
             print("You don't have sufficient balance")

    
    def deposite(self):
        self.depo=int(input("Enter Amount you want to Deposit:"))
        if self.depo>0:
            n=customer['bal']+self.depo
            print("Deposite sucessfuly")
            print("your current balance is:",n)
            customer['bal']=n
        else:
            print("Your amount should be greater than zero:")
    
    def view_balance(self):
        print("View Balance")
        print(f"Your Total Balance is:{customer['bal']}")

    