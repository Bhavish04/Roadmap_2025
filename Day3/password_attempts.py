correct_password="Bhavish@123"
attempts=0
while attempts<3:
    user_input=input("Enter your password")
    if user_input==correct_password:
        print("Permission Granted")
        break
    else:
        print("Incoorect Password")
        attempts+=1
else:
    print("Access Denied")