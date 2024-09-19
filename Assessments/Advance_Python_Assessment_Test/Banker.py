auth={}
class Banker:
    def register(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
                        
        auth['Username'] = self.username
        if self.username in auth:
                print("Customer already exists.")
        else:
            auth['Password']=self.password
            print("Register Successfully")
            print(auth)
    

    def login(self):
        self.username = input("Enter username: ")
        if self.username in auth['Username']:
            self.password = input("Enter password: ")
            if auth['Password'] == self.password:
                print("Log in successfully.")
            else:
                print("Invalid password.")
        else:
            print("Invalid username.")
        print(auth)
    

    def update_customer(self):
        self.username = input("Enter customer username to update: ")
        if self.username in auth['Username']:
            self.new_password = input("Enter new password: ")
            auth['Password'] = self.new_password
            print("Customer password updated successfully.")
        else:
            print("Customer not found.")

    
    def view_customer(self):
        if not auth:
            print("No customers registered.")
        else:
            for username in auth.keys():
                if username == 'Username':
                    print(f"Customer Username: {auth[username]}")

    def delete_customer(self):
        self.username = input("Enter customer username to delete: ")
        for customer in auth:
            if customer['Username'] == self.username:
                auth.remove(customer)
                print("Customer deleted successfully.")
        else:
            print("Customer not found.")

     
        