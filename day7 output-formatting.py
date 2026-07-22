'''
                         Output Formatting
                        ------------------------
1.Comma seperation(,)

Example: comma seperated
name = 'bannu'
age = 21
print('Welcome', name, 'Your age is', age)
------------------------------------------------------

2.F-string (doc-string)

example:

name = 'bannu'
age = 21
print('Welcome', name, 'Your age is', age)
print(f'Welcome {name} Your age is {age}')
--------------------------------------------------------
--------------------------------------------------------

Modulus Operators

%s --> allows all types of data types
example:

name = 'bannu'
print('Name : %s' % name)
---------------------------------------
%d --> digits
example:

age = 21
print('Age : %d' % age)
-----------------------------------------
%f --> float values
example:

price = 100.89
print('Price : %f' % price)

--------------------------------------------------------------
--------------------------------------------------------------

(dot) .format()
-----------------
example:

name = 'bannu'
age = 21
print('Name : {} \nage : {}'.format(name,age))
----------------------------------------------------------------
----------------------------------------------------------------




                                                                            Statements
                                                                            -------------
                                                                            -------------

1. condition
-------------
-------------
if condition
------------
- the if condition is used to check if it is TRUE or FALSE

example:

age = int(input("Enter your age: "))
if age >= 18:
    print(f'your age is {age} and you are eligible to vote')
-----------------------------------------------------------------
if-else condition
-----------------
- else is the fall-back statement, incase if condition is false then this else block will execute...

example:

name = input("Enter your name:")
age = int(input("Enter your age: "))
if age >= 18:
    print(f'Hii {name}, Your age is {age} and you are eligible to vote')
else:
    print(f'Hii {name}, You are not eligible to vote, you have to wait {18 - age} years, to vote')
------------------------------------------------------------------------------------------------------



Simple code examples:
--------------------------
--------------------------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f' {num} is a even number')
else:
    print(f' {num} is a odd number')
-----------------------------------------

v = input('Enter a single letter:')
if v in 'AaEeIiOoUu':
    print(f' {v} is vowel')
else:
    print(f' {v} is consonant')
-------------------------------------------

num = input('Enter a word: ')
nums = num[::-1]
if num == nums:
    print(f' {num} is palindrome')
else:
    print(f' {num} is not a palindrome')
------------------------------------------------

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f' {year} is a leap year')
else:
    print(f' {year} is not a leap year')
-----------------------------------------------------

f1 = input(f'Enter Friend 1 name: ')
f2 = input(f'Enter Friend 2 name: ')
f3 = input(f'Enter Friend 3 name: ')
h1 = input(f'Enter height of {f1} in cm: ')
h2 = input(f'Enter height of {f2} in cm: ')
h3 = input(f'Enter height of {f3} in cm: ')

if h1 > h2 and h1 > h3:
    print(f' {f1} is taller than {f2} and {f3}.')
if h2 > h3 and h2 > h1:
    print(f' {f2} is taller than {f1} and {f3}.')
if h3 > h1 and h3 > h2:
    print(f' {f3} is taller than {f1} and {f2}.')  
'''
