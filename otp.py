import random

dicts = {"Name" : "Bannu",
             "Age" : 21,
             "PIN" : "1311",
             "Balance" : 10000}
print(f'Welcome {dicts["Name"]} to Axis Bank!')
remain = 3
while remain > 0:
    pin = input("Enter your 4 digit pin: ")
    if len(pin) == 4:
        if pin == dicts['PIN']:
            otp = random.randint(10000, 99999)
            print(otp)
            otps = int(input("Enter your 6 digit OTP :"))
            if otps == otp:
                opt = int(input("Select options \n1.Withdraw \n2.Deposit \n3.Check Balance"))
            else:
                print("You have entered incorrect otp")
        else:
            remain -= 1
            if remain > 0:
                print(f'Incorrect otp enetered and you have {remain} remaining chances')
            else:
                print(f'You have entered 3 incorrect pins')
    else:
        print("Please enter only 4 digit otp")
    
    
