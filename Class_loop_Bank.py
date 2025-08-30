from datetime import datetime,date
class Bank_Acc:
    presentDay=date.today().strftime("%d/%m/%Y")
    Global_acc_No = 5000000000  # Class variable for auto-incrementing account numbers
    Global_bank_name="Central Bank of India"
    Global_BankBranch="KPHP"
    Global_iFsC="CBIN00123"
    def __init__(self):
        self.name = ""
        self.dob = None
        self.age=None
        self.ifsc = ""
        self.account_No = None
        self.PhoneNo=None
        self.Branch=""
        self.address=None
        self.balance=0
    @staticmethod
    def holders_age(dob):
        from Tausif_op import age_calculator as age_c
        BDay=int(dob[:2])
        BMonth=int(dob[3:5])
        BYear=dob[6:]
        age_year=age_c(BDay,BMonth,BYear)
        return age_year
    def create_Account(self):
        self.name = input("Enter account holder's name: ")
        while True:
            self.dob = input("Enter your date of birth (DD/MM/YYYY): ")
            try:
                dob_obj=datetime.strptime(self.dob,"%d/%m/%Y")
                break
            except ValueError:
                print("Date Format is Wrong:")
        self.age=Bank_Acc.holders_age(self.dob)
        if self.age<15:
            print("!You are Below Legal Age!")
            self.name=""
            self.dob=None
            print("Account creation cancelled. All data has been erased.")
        else:
            while True:
                try:
                    self.PhoneNo=int(input("Enter 10 digit Phone Number:"))
                    if len(str(self.PhoneNo))!=10:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid phone number. Please enter a 10-digit number.")
            self.ifsc=Bank_Acc.Global_iFsC
            self.Branch=Bank_Acc.Global_BankBranch
            self.address=input("House No:\tArea:\tLandMark:\tDist:\tPIN:\tState:")
            choice = input("Do you want to create the account? (y/n): ")
            if choice.lower() == 'y':
                Bank_Acc.Global_acc_No += 1
                self.account_No = Bank_Acc.Global_acc_No
                print(f"Account created successfully! Your account number is {self.account_No}")
            else:
                # Clear all previously entered values
                self.dob = None
                self.age=None
                self.ifsc = ""
                self.name = ""
                self.account_No = None
                self.PhoneNo=None
                print("Account creation cancelled. All data has been erased.")
    def Deposit(self):
        amount=int(input("Enter the Deposit Amount:"))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance+=amount
        print(f"₹:{amount} credited to Ac.No:{self.account_No} on {Bank_Acc.presentDay}\n Total Available balance:{self.balance}")
    def withdrawal(self,mobile):
        from Tausif_op import send_otp as so
        Amount=int(input("Enter the withdrawal amount:"))
        if Amount<=0 or Amount>self.balance:
            print("Withdrawal amount must be positive and less then balance:")
            return
        otp_send=so(mobile,Amount)
        try:
            otp_recieved = int(input("Enter the OTP received:"))
        except ValueError:
            print("Invalid OTP format.")
            return
        if otp_send==otp_recieved:
            print("OTP varified!")
            self.balance-=Amount
            print(f"₹:{Amount} withdrawn from Account NO:{self.account_No} on {Bank_Acc.presentDay}\n Total Available balance:{self.balance}")
        else:
            print("cannot Whitdraw Money!")
            return
    def display_Account(self):
        print("-" * 10, f"{self.Global_bank_name}", "-" * 10)
        print(f"Account Holder's Name   : {self.name}")
        print(f"DOB                     : {self.dob}")
        print(f"Age                     : {self.age}")
        print(f"Phone No                : {self.PhoneNo}")
        print(f"Address                 : {self.address}")
        print(f"Bank Branch             : {self.Branch}")
        print(f"IFSC Code               : {self.ifsc}")
        print(f"Account Number          : {self.account_No}")
        print(f"Current Balance         : ₹{self.balance}")