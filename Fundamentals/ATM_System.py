balance = 1000.0

# Introduction
print("=====================")
print("💳 SMART ATM SYSTEM")
print("=====================")

# validating Pin
pin = int(input("Enter Your PIN: "))
if pin == 2275:
    while True:
        print("1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")


        print("================================")
        choice = int(input("Enter Your Choice: "))
        match choice:
            # Balance Functionality
            case 1:
                print("The Balance is: ", balance)
                print("================================")

            # Deposit Functionality
            case 2:
                deposit = float(input("Enter Amount to Deposit: "))
                if deposit < 0:
                    print("OOPS! , Can't Deposit -ve amount 😅")
                    print("================================")
                    continue
                balance += deposit
                print("The Balance is Updated 😎: ", balance)
                print("=====================================")

            # Withdraw Functionality
            case 3:
                withdraw = float(input("Enter Amount to Withdraw: "))
                if withdraw > balance or withdraw < 0:
                    print("OOPS! , Can't withdraw this amount 😅")
                    print("================================")
                    continue
                balance -= withdraw
                print("The Balance is Updated 🫡: ", balance)
                print("================================")

            # Exiting the bank
            case 4:
                print("Thank you for using Smart ATM , Have a nice day!!!")
                break
            case _:
                print("Invalid Choice , Please use a valid choice ☺️")
                print("==============================================")

else:
    print("Authorization failed")








