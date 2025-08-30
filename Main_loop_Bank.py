from Storage_Bank import save_accounts, load_accounts
from Class_loop_Bank import Bank_Acc
Acc_holder = load_accounts()
while True:
    choice=int(input(f"Enter 1 To create a Account:\nEnter 2 to Display Account Details:\n"
                     "Enter 3 to Deposite:\nEnter 4 to whithdrow money:\nTo logout press 0:"))
    save_accounts(Acc_holder)
    match choice:
        case 1:
            acc_obj=Bank_Acc()
            acc_obj.create_Account()
            if acc_obj.account_No is not None:
                Acc_holder[acc_obj.account_No] = acc_obj
            save_accounts(Acc_holder)
        case 2:
            lookup=int(input("Enter your Account Number:"))
            if lookup in Acc_holder:
                Acc_holder[lookup].display_Account()
            else:
                print("Account Not found!")
            save_accounts(Acc_holder)
        case 3:
            lookup=int(input("Enter You Account Number:"))
            if lookup in Acc_holder:
                Acc_holder[lookup].Deposit()
            else:
                print("Account not found!")
            save_accounts(Acc_holder)
        case 4:
            lookup=int(input("Enter Your Account Number:"))
            phoneNo=int(input("Enter your registered number to verify:"))
            if lookup in Acc_holder:
                if Acc_holder[lookup].PhoneNo!=phoneNo:
                    print("Number do not exist!")
                else:
                    mobile='+91'+str(phoneNo)
                    Acc_holder[lookup].withdrawal(mobile)
            else:
                print("Account not found!")
            save_accounts(Acc_holder)
        case 0:
            print("See you again")
            save_accounts(Acc_holder)
            break
        case _:
            print("Invalid Choice please enter valid choice:")
        


        

    