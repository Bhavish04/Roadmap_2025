balance=10000
while True:
    print("\n====ATM Menu====")
    print("1.Check Balance")
    print("2Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Your Balance is $",balance)
    elif choice==2:
        deposit=int(input("Enter the amount to be deposited"))
        balance+=deposit
        print("$",deposit,"Deposit Successfull")
    elif choice==3:
        withdraw=int(input("Enter the amount to withdraw"))
        if withdraw>balance:
            print("Insufficient balance")
        else:
            balance-=withdraw
            print("$",withdraw,"withdrawn successfully")
    elif choice==4:
        print("Thank you for using our ATM")
        break
    else:
        print("Invalid Choice,Try again")