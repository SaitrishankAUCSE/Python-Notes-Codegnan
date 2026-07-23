'''

elif
----
example:

marks = int(input("Enter marks: " ))
if marks >= 90:
    print('A+')
elif marks >= 80:
    print('A')
elif marks >= 70:
    print('B+')
elif marks >= 60:
    print('B')
elif marks >= 50:
    print('C+')
elif marks >= 40:
    print('C')
else:
    print('Fail')
------------------------------------

num1 = int(input("Enter value of 1st Number: "))
num2 = int(input("Enter value of 2nd Number: "))
num3 = int(input("Enter value of 3rd Number: "))

if num1 > num2 and num1 > num3:
    print(f' {num1} is greater among three numbers')
elif num2 > num1 and num2 > num3:
    print(f' {num2} is greater among three number')
else:
    print(f' {num3} is greater among three numbers')
------------------------------------------------------------

nested if
----------
example:

details = {'ATMPIN' : '8219'}

atmpin = input("Enter your 4 digit ATM pin: ")
if len(atmpin) == 4:
    if atmpin == details['ATMPIN']:
        options = int(input("Choose \n1.Withdraw \n2.Deposit \n3.Pin Change \nChoose one option: "))
        if options == 1:
            moneyw = int(input("Enter amount to withdraw: "))
            print(f' {moneyw} has been debited from your account')
        elif options == 2:
            moneyd = int(input("Enter amount to deposit: "))
            print(f' {moneyd} has been credited to your account')
    else:
        input("You entered incorrect pin: \nPlease enter again: ")
else:
    input("Please enter 4 digit pin only: ")


---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
CONTROL STATEMENTS
-------------------------
-------------------------
1. break
- stops when the given condition is met

example:
num = [1,23,4,67,645,86,45,7]

for i in num:
    print(i)
    if i == 4:
        break
-----------------------------------------------

2. continue
- skips the particular given condition and continues the remaining execution

example:
num = [1,25,4,76,5,8,45,6]
for i in num:
    if i == 4:
        continue
    print(i)

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
LOOPS
----------
----------
1.for loop
-----------
- for loop is used to iterate over sequence such as str, list, tuple
- else in for loop, it will execute  when whole iteration is completed....
- incase if condition becomes true, then else will never execute....

example:
num = "Python is a language"
for i in num:
    print(i)
----------------------------------------------------------------------------------
range() - function is used to generate number upto a limit
syntax - range(start, end, step)
example:

for i in range(1, 10, 2):
    print(i)
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
2. while loop
--------------
- the loop runs until a certain condition remains true, if the condition fails, the loop stops

exmaple:

num = int(input("Enter a number: "))
nums = int(input("Enter limit: "))
while num < nums:
    print(num)
    num += 5
------------------------------------------------------------------------------------------------------------

ASSERT keyword
- the keyword is used to check the condition

example:
age = int(input("Enter age: "))
assert age >= 18, 'Not eligible you'
print('Eligible')

example:
marks = int(input("Enter marks: "))
assert marks >= 35, 'you have failed'
print('pass')
'''
''''
details = {'ATMPIN' : '8219'}

atmpin = input("Enter your 4 digit ATM pin: ")
if len(atmpin) == 4:
    if atmpin == details['ATMPIN']:
        options = int(input("Choose \n1.Withdraw \n2.Deposit \n3.Pin Change \nChoose one option: "))
        if options == 1:
            moneyw = int(input("Enter amount to withdraw: "))
            print(f' {moneyw} has been debited from your account')
        elif options == 2:
            moneyd = int(input("Enter amount to deposit: "))
            print(f' {moneyd} has been credited to your account')
    else:
        input("You entered incorrect pin: \nPlease enter again: ")
else:
    input("Please enter 4 digit pin only: ")
'''

times = input("Enter time in 24 hours: ")
parts = times.split(':')
hours = int(parts[0]) - 12
if hours > 12:
    print(f' {parts[0] - 12} : {parts[1]} PM')
elif hours < 12:
    print(f' {parts[0]} : {parts[1]} PM')
