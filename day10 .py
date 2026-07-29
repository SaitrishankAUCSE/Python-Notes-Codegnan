'''
program: simple table print:

num = int(input("Enter number: "))
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')
-----------------------------------------
program: to check if a number is armstrong number or not:

num = int(input("Enter number: "))

length = len(str(num))

am = 0
for i in str(num):
    am = int(i) ** length + am
if am == num:
    print(f' {num} is a armstrong number')
else:
        print(f' {num} is not a armstrong number: \nPlease try again: ')
-----------------------------------------------------------------------------
program: fibonacci series:

limit = int(input("Enter a limit: "))

num1 = 0
num2 = 1

print(num1, num2, end =' ')
for i in range(1, limit):
    total = num1 + num2
    num1 = num2
    num2 = total
    print(total, end= ' ')
---------------------------------------------------------------------------
program: calculator

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
op = int(input("\n1.ADDITION: \n2.SUBTRACTION: \n3.MULTIPLICATION: \n4.DIVISION: \n5.POWER: \n\nEnter Option: "))

if op == 1:
    print(num1 + num2)
elif op == 2:
    print(num1 - num2)
elif op == 3:
    print(num1 * num2)
elif op == 4:
    print(num1 / num2)
elif op == 5:
    print(num1 ** num2)
------------------------------------------------------------------------------
------------------------------------------------------------------------------
practice coding:
1. check whether a number is positive or negative number:

num = int(input("Enter a number: "))
if num > 0:
    print(f'The {num} is a positive number')
else:
    print(f'The {num} is a negative number')
---------------------------------------------------------------------------------
2. check if the given string is a palindrome or not:

string = input("Enter a string: ")
if string == string[::-1]:
    print(f'The string {string} is a palindrome')
else:
    print(f'The string {string} is not a palindrome')
----------------------------------------------------------------------------------
3. fibonacci series:

limit = int(input("Enter limit to print fibonacci series: "))
num1 = 0
num2 = 1
print(num1, num2, end = ' ')
for i in range(1, limit):
    total = num1 + num2
    num1 = num2
    num2 = total
    print(total, end = ' ')
-----------------------------------------------------------------------------------
4. check age and return True if age is less than 55:

age = int(input("Enter age: "))

if age <= 55:
    print(True)
else:
    print(False)
-------------------------------------------------------------------------------------
5.
city = input("Enter city name: ")

if city == 'vizag':
    print("A")
elif city == 'vijayawada':
    print("B")
elif city == 'vizag, vijayawada':
    print("C")
elif city != 'vizag' and 'vijayawada':
    print("D")
----------------------------------------------------------------------------------------
'''
city = input("Enter city name: ")

if city == 'vizag':
    print("A")
elif city == 'vijayawada':
    print("B")
elif city == 'vizag, vijayawada':
    print("C")
elif city != 'vizag' and 'vijayawada':
    print("D")
