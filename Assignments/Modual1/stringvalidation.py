name=input("Enter Your Name: ")
if name.isalpha():
    print("success")
 
age=input("Enter Your Age: ")
if age.isdigit():
    print("Suceess")

email=input("Enter Your Email Address: ")
if email.islower():
    print("Suceess")

pwd=input("Enter Your Password: ")
cnfpwd=input("Enter Your Confirm Password: ")
if pwd==cnfpwd:
    print("Sucess")
    
mbno=input("Enter Your Mobile Number: ")
if mbno.isdigit(): 
    print("Success")


