from otp import *
import random

ICICI_Bannu = {
    'Name': 'Bannu Sai',
    'Acc_No': '1234567890',
    'Aadhar': '0000 0000 0000',
    'Pan': '1234567890',
    'ATMPIN': '1311',
    'PASSWORD': 'bannusai1311',
    'Balance': 1000
}

remain = 3
otp_remain = 3
transaction = []

print(f"Hi, {ICICI_Bannu['Name']}")
print("Welcome to ICICI BANK\n")
print("Please insert your ATM card")

while remain > 0:

    pin = input("Enter your 4 digit PIN: ")

    if len(pin) != 4:
        print("Please enter only a 4 digit PIN.\n")
        continue

    if pin == ICICI_Bannu['ATMPIN']:

        otp = random.randint(100000, 999999)
        print(otp)

        user_otp = int(input("Enter your 6 digit OTP: "))

        while otp_remain > 0:
            if otp == user_otp:

                while True:

                    print("\n========== ICICI ATM ==========")
                    print("1. Withdraw")
                    print("2. Deposit")
                    print("3. Check Balance")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Fund Transfer")
                    print("7. Exit")

                    opt = int(input("\nSelect Option: "))

                    # Withdraw
                    if opt == 1:

                        withdraw_money = int(input("Enter amount to withdraw: "))

                        if withdraw_money > ICICI_Bannu['Balance']:
                            print("Insufficient funds.")

                        elif withdraw_money % 100 != 0:
                            print("Amount should be in multiples of 100.")

                        else:
                            ICICI_Bannu['Balance'] -= withdraw_money
                            print(f"\n{withdraw_money} withdrawn successfully.")
                            print(f"Remaining Balance: {ICICI_Bannu['Balance']}")
                            transaction.append(f"Withdraw {withdraw_money}")

                    # Deposit
                    elif opt == 2:

                        deposit_money = int(input("Enter amount to deposit: "))

                        if deposit_money % 100 == 0:
                            ICICI_Bannu['Balance'] += deposit_money
                            print(f"\n{deposit_money} deposited successfully.")
                            print(f"Current Balance: {ICICI_Bannu['Balance']}")
                            transaction.append(f"Deposit {deposit_money}")

                        else:
                            print("\nAmount should be in the form of 100 or 500 or 2000 notes.")

                    # Check Balance
                    elif opt == 3:

                        print(f"\nAvailable Balance: {ICICI_Bannu['Balance']}")

                    # Change PIN
                    elif opt == 4:

                        old_pin = input("Enter your old PIN: ")

                        if old_pin == ICICI_Bannu['ATMPIN']:

                            new_pin = input("Enter new 4 digit PIN: ")

                            if len(new_pin) == 4:
                                ICICI_Bannu['ATMPIN'] = new_pin
                                print("PIN changed successfully.")
                            else:
                                print("PIN must contain exactly 4 digits.")

                        else:
                            print("Incorrect PIN.")

                    # Transaction History
                    elif opt == 5:

                        if len(transaction) == 0:
                            print("\nNo transactions found.")

                        else:
                            print("\n------ Transaction History ------")

                            for i in range(len(transaction)):
                                print(f"{i+1}. {transaction[i]}")

                    # Fund Transfer
                    elif opt == 6:

                        receiver_acc = input("\nEnter the receiver Account No.: ")
                        receiver_name = input("Enter the receiver Name: ")
                        receiver_money = int(input("Enter amount to be transferred: "))
                        receiver_pin = input("Enter your PIN: ")

                        if receiver_pin == ICICI_Bannu['ATMPIN']:

                            if receiver_money <= ICICI_Bannu['Balance']:
                                ICICI_Bannu['Balance'] -= receiver_money

                                print(f"{receiver_money} is transferred successfully to {receiver_name}")
                                print(f"Available Balance is {ICICI_Bannu['Balance']}")

                                transaction.append(f"Transfer {receiver_money} to {receiver_name}")

                            else:
                                print("Insufficient Balance.")

                        else:
                            print("Your PIN is incorrect.")

                    # Exit
                    elif opt == 7:

                        print("\nThank you for banking with ICICI.")
                        exit()

                    else:
                        print("Invalid Option.")

            else:
                otp_remain -= 1
                print(f'Incorrect OTP. and you have still {otp_remain} chances.')

        else:

            remain -= 1

            if remain > 0:
                print(f"Incorrect PIN. {remain} attempts remaining.\n")

            else:
                print("Your card has been blocked.")

