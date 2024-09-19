from Banker import Banker
from Customer import Customer

def main():
    while True:
        print(f"\nWELCOME TO BANK MANAGEMENT SYSTEM\n")
        print(f"1) Banker")
        print(f"2) Customer\n")
        print(f"3) Exit\n")

        choice=input('choose your role :')

        if choice == '1':
            banker = Banker()
            while True:
                print("\nBanker Menu")
                print("1. Register")
                print("2. Login")
                print("3. Update Customer")
                print("4. View Customers")
                print("5. Delete Customer")
                print("6. Exit")

                option = input("Enter your choice: ")

                if option == '1':
                    banker.register()
                elif option == '2':
                    banker.login()
                elif option == '3':
                    banker.update_customer()
                elif option == '4':
                    banker.view_customer()
                elif option == '5':
                    banker.delete_customer()
                else:
                    break


        elif choice=='2':
            customer=Customer()
            while True:
                print("\nCustomer Menu")
                print("1. Register")
                print("2. Login")
                print("3. Withdraw Amount")
                print("4. Deposite Amount")
                print("5. View Balance")
                print("6. Exit")

                option = input("Enter your choice: ")

                if option == '1':
                    customer.register()
                elif option == '2':
                    customer.login()
                elif option == '3':
                    customer.withdraw()
                elif option == '4':
                    customer.deposite()
                elif option == '5':
                    customer.view_balance()
                else:
                    break
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")
main()