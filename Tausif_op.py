def table(num):
    '''Takes integer value as argument\n
    Prints the multiplication Table from 1 to argument value\n
    Does not returns any value'''
    for i in range(1,num+1):
        for j in range(1,11):
            print(f"{i}*{j}={i*j}",end="\t")
        print()
def greetName(name):
    from datetime import datetime as tm
    current_time=tm.now().time()
    Op_time=current_time.strftime("%I:%M:%S %p")
    print(f"----------------Current time:{Op_time}----------------")
    hour=current_time.hour
    def greetTime(hour):
        if (0<hour<=4) or (15<hour<=21):
            return "Good Evening"
        elif (4<hour<12):
            return "Good Morning"
        elif (12<=hour<=15):
            return "Good Afternoon"
        else:
            return "Good Night"
    for n in name:
        if n.lower().startswith('s'):
            greetGreat=greetTime(hour)
            print(f"{greetGreat} {n}")
def prime(num):
    i=2
    while(i<num):
        if(num%i==0):
            print(f"{num} is Not Prime")
            break
        i+=1
    if(i==num):
        print(f"{num} is prime")
def Range(r):
    i=1
    var=0
    while i<=r:
        var+=i
        i+=1
    return (f"Sum of first {r} natural numbers is:{var}")
def factorial(num):
    fact=1
    fact_list=[]
    for i in range(1,num+1):
        fact_list.append(i)
        fact*=i
    return fact,fact_list
def febonacci(r):
    if r<0:
        return []
    if r==0:
        return [0]
    feb_list=[0,1]
    for _ in range(2,r+1):
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
def F_convert(f):
    return 5*(f-32)/9
def is_prime(num):
    import math as m
    n=int(m.sqrt(num))
    for i in range(2,n+1):
        if (num%i==0):
            break
    else:
        return (f"{num} is Prime Number")
def age_calculator(BirthDay,BirthMonth,BirthYear):
    from datetime import date
    PresentDate=date.today()
    PresentDay=int(PresentDate.day)
    PresentMonth=int(PresentDate.month)
    PresentYear=int(PresentDate.year)
    # PresentDate=PresentDate.strftime("%d-%m-%y")

# perfroming the substraction between present date and  Birth date
    def age(Pyear,Pmonth,Pday,Byear,Bmonth,BDay):
        ageYear=Pyear-Byear
        ageMonth=Pmonth-Bmonth
        ageDay=Pday-BDay
        return {'year':ageYear}
    
    if (len(BirthYear)==4) and BirthYear.isdigit() and (BirthDay<=31)and(BirthMonth<=12)and(BirthDay>=1)and(BirthMonth>0):
        BirthYear=int(BirthYear)
        if BirthYear>PresentYear:  
            return "Not Born"
        #code for calculating the age 
        elif(PresentMonth<BirthMonth):
            year1=PresentYear-1
            if(PresentDay>=BirthDay):
                month1=PresentMonth+12
                resultage=age(Pyear=year1,Pmonth=month1,Pday=PresentDay,Byear=BirthYear,Bmonth=BirthMonth,BDay=BirthDay)
                return resultage["year"]
            elif(PresentDay<BirthDay):
                month1=PresentMonth+11
                day1=PresentDay+30
                resultage=age(Pyear=year1,Pmonth=month1,Pday=day1,Byear=BirthYear,Bmonth=BirthMonth,BDay=BirthDay)
                return resultage["year"]
        elif(PresentMonth>=BirthMonth): 
            if(PresentDay>=BirthDay):
                resultage=age(Pyear=PresentYear,Pmonth=PresentMonth,Pday=PresentDay,Byear=BirthYear,Bmonth=BirthMonth,BDay=BirthDay)
                return resultage["year"]
            elif(PresentDay<BirthDay):
                month1=PresentMonth-1
                day1=PresentDay+30
                resultage=age(Pyear=PresentYear,Pmonth=month1,Pday=day1,Byear=BirthYear,Bmonth=BirthMonth,BDay=BirthDay)
                return resultage["year"]
    else:
        print("Wrong Input")
def send_otp(phone_number,amount):
    from twilio.rest import Client
    import random
    # Generate 6-digit OTP
    otp = random.randint(100000, 999999)

    # Twilio credentials (you get these from your Twilio account)
    account_sid = 'AC9792fbcd2b5889a978000cc6102aa8c1'
    auth_token = '03366ea8c224516747e82ecc1f8dad74'
    twilio_number = '+19206575938'  # Your Twilio phone number
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f'Your OTP is: {otp}\nFor the Transection of Rs.{amount}',
        from_=twilio_number,
        to=phone_number
    )
    print(f'OTP sent to {phone_number}')
    return otp  # You can use this to validate user input later

# Example usage:
# otp_sent = send_otp('+918134992573')
# user_otp = int(input("Enter the OTP received: "))
# if user_otp == otp_sent:
#     print("OTP Verified")
# else:
#     print("Invalid OTP")



