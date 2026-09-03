'''
#1.print the area of an rectangle by length and breadth
length = int(input("Enter length of the rectangle: "))
breadth = int(input("Enter breadth of the rectangle :"))
area = length * breadth
print(f'The area of rectangle is {area}')
--------------------------------------------------------------

#2.Take input as name and age and greet them
name = input("Enter name :")
age = int(input("Enter age: "))
print(f'Hi {name}, welcome to Python, glad to have people of {age} like you.')
-----------------------------------------------------------------------------------

#3.Even number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f'The number {num} is Even')
else:
    print(f'The number {num} is Odd')
-----------------------------------------------------------------------------------
#4.print maximum and minimum number in the list  
numbers = list(map(int, input("Enter elements in list :").split()))
print(f'The maximum number in the list is {max(numbers)}')
print(f'The minimum number in the list is {min(numbers)}')
--------------------------------------------------------------------------------------

#5.to check if the string is palindrome or not
string = input("Enter the string: ")

if string == string[::-1]:
    print(f'The string is a palindrome')
else:
    print(f'The string is not a palindrome')
-----------------------------------------------------------------------------------------------

#6.To take days as input and count how many weeks , years
days = int(input("Enter number of days : "))

years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print("Years =", years)
print("Weeks =", weeks)
print("Days =", days)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#7.
print(5 & 3)
print(6 & 9)

------------------------------------
#8.
name = input("Enter your name: ")

for i in range(1, 1516):
    print(i, name)
-------------------------------------
string = input("Enter string: ")
floats = float(string)
print(floats)
print(type(floats))
---------------------------------------
#9.
num = int(input("Enter a number:"))
floats = float(num)
print(num)
print(type(floats))
--------------------------------------
#10.
char = input("Enter a character: ")
ints = int(char)
print(ints)
print(type(ints))
------------------------------------------------------
#11.
for i in range(4):
    for j in range(4):
        print('*', end=' ')
    print()
    
         (or)
         
for i in range(4):
    print('****')
--------------------------------------------------------- 
#12.
num = int(input("Enter a number: "))

if num % 1 == 0 and num % num == 0:
    print(f'The number {num} is PRIME number')
else:
    print(f'The number {num} is not a PRIME number')
if num ==  int(str(num)[::-1]):
    print(f'The number is a palindrome')
else:
    print(f'The number is not a palindrome')

if (num % 1 == 0 and num % num == 0) and  int(str(num)[::-1]):
    print(f'The number {num} is both PRIME and PALINDROME number')
-----------------------------------------------------------
-----------------------------------------------------------
date: 01-08-2026
#print satrs

num = 5

for i in range(1, 6):
    print('*' * num)
    num -= 1
for j in range(2,6):
    print('*' * j)
    j-=1

------------------------------------------------------------

for i in range(1, 6):
    for j in range(1 , i+1):
        print(j, end = ' ')
    print()

for i in range(4, 0, -1):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()
--------------------------------------------------------------

lists = ['A', 'B', 'C', 'D', 'E']

for i in range(1, 6):
    for j in range(i):
        print(lists[j], end= ' ')
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print(lists[j], end = ' ')
    print()

for i in range(1, 6):
    for j in range(i):
        print(lists[j], end= ' ')
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print(lists[j], end= ' ')
    print()
---------------------------------------------------
---------------------------------------------------
lists = "A B C D E".split()

for i in range(1, 6):
    print(" ".join(lists[:i]))

for j in range(4, 0, -1):
    print(" ".join(lists[:j]))

for i in range(1, 6):
    print(" ".join(lists[:i]))

for j in range(4, 0, -1):
    print(" ".join(lists[:j]))

for i in range(1, 6):
    print(" ".join(lists[:i]))

for j in range(4, 0, -1):
    print(" ".join(lists[:j]))po
----------------------------------------------------------------------------------------------------------------------

    04th august 2026
    ----------------
    ----------------

from day15 import *             
print(add(5,6))
print(mul(2,3))
print(sub(10,5))
print(div(10,2))
print(pow(2,3))
---------------------------------------------------------

import day15

day15.display("bannu")
----------------------------------------------------------

import random
l = ['banana', 'apple', 'mango', 'grapes', 'orange', 'kiwi', 'watermelon', 'pineapple', 'papaya', 'pear']
ans = l[random.randint(0, len(l)-1)]
print(ans)



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#1.print the area of an rectangle by length and breadth
length = int(input("Enter length of the rectangle: "))
breadth = int(input("Enter breadth of the rectangle :"))
area = length * breadth
print(f'The area of rectangle is {area}')
--------------------------------------------------------------

#2.Take input as name and age and greet them
name = input("Enter name :")
age = int(input("Enter age: "))
print(f'Hi {name}, welcome to Python, glad to have people of {age} like you.')
-----------------------------------------------------------------------------------

#3.Even number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f'The number {num} is Even')
else:
    print(f'The number {num} is Odd')
-----------------------------------------------------------------------------------
#4.print maximum and minimum number in the list  
numbers = list(map(int, input("Enter elements in list :").split()))
print(f'The maximum number in the list is {max(numbers)}')
print(f'The minimum number in the list is {min(numbers)}')
--------------------------------------------------------------------------------------

#5.to check if the string is palindrome or not
string = input("Enter the string: ")

if string == string[::-1]:
    print(f'The string is a palindrome')
else:
    print(f'The string is not a palindrome')
-----------------------------------------------------------------------------------------------
#6.to calculate compoud interest:
principal = int(input("Enter principal amount: "))
rate = int(input("Enter interest rate: "))
time = int(input("Enter time: "))
n = 1

r_decimal = rate / 100
total_amount = principal * ((1 + (r_decimal / n)) ** (n * time))
interest_earned = total_amount - principal

print(principal)
print(round(total_amount, 2))
print(round(interest_earned, 2))
------------------------------------------------------------------------------------------------
#7.To take days as input and count how many weeks , years
days = int(input("Enter number of days : "))

years = days // 365
days = days % 365

weeks = days // 7
days = days % 7

print("Years =", years)
print("Weeks =", weeks)
print("Days =", days)
-------------------------------------------------------------------------------------------------

#8. Sum of all positive numbers in a list:
nums = list(map(int, input("Enter numbers with space: ").split()))
for i in range(len(nums)):
    if i > 0:
        s=sum(nums)
print(s)
-----------------------------------------------------------------------------------------------------

#9.count the number of words in a sentence:
name = input("Enter a sentence: ")
n = name.split()
print(len(n))
-------------------------------------------------------------------------------------------------------------

#10.swapping of two variables:
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print(a, b)
a, b = b, a
print("After swapping: ", a, b)
---------------------------------------------------------------------------------------------------------

#11.find sum and averge of elements in a list:
nums = list(map(int, input("Enter numbers with space: ").split()))

s = sum(nums)
avg = s/len(nums)
print("Sum of numbers is: ", s)
print("Average of numbers is: ", avg)
--------------------------------------------------------------------------------------------------------------

#12.Temperature conversion from celcius to kelvin:
temp = int(input("Enter temperature in celcius: "))

print("Kelvin temperature is: ", temp+273.15)
-------------------------------------------------------------------------------------------------------------------------

#13.check if a string is palindrome or not:
name = input("Enter a string: ")
if name == name[::-1]:
    print(f'the string {name} is a palindrome')
else:
    print(f'the string {name} is not a palindrome')
-------------------------------------------------------------------------------------------------------------

#14.function for reversing a string:
def reverse(name):
    return name[::-1]

name = input("Enter a name: ")
print(reverse(name))
---------------------------------------------------------------------------------------------------------

#15.concatenate list of names into single string:
names = input("Enter names: ").split()
ans = " ".join(names)

print(ans)
-----------------------------------------------------------------------------------------------------------------------

#16.pangram:
name = input("Enter a sentence: ")
n = name.lower()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
input_set = set(n)
if alphabet.issubset(input_set):
    print("It is a pangram")
else:
    print("It is not a pangram")
----------------------------------------------------------------------------------------------------------------------------------

#17. Calculate area and circumference:
radius = int(input("Enter radius: "))
area = 3.14 * radius**2
cir = 2 * 3.14 * radius
print(area, ",", cir)
--------------------------------------------------------------------------------------------------------------------------

#18. convert minutes to hours and minutes:
mins = int(input("Enter number of minutes: "))
hour = mins // 60

remaining = mins % 60
print(f' {hour} hours, {remaining} minutes')
-------------------------------------------------------------------------------------------------------------------------------------

#19. To create a function to count the number of vowels in a given string
def stringsvow(strings):
    vow = "aeiouAEIOU"
    c = 0
    if strings == "":
        return "No Vowels"
    else:
        for i in strings:
            if i in vow:
                c += 1
        return c

strings = input("Enter a string: ")
print(stringsvow(strings))
-------------------------------------------------------------------------------------------------------------------------

#20. To check is a number is prime 
n  = int(input("Enter a number: "))

if n//1 == 0 and n//n == 0:
    print(f'{n} is prime number')
else:
    print(f'{n} is not a prime number')
---------------------------------------------------------------------------------------------------------------
'''
#21. Class to represent a basic calculator

class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def data(self):
        print(self.title)
        print(self.author)
        print(self.year)

b1 = book("PUK", 'Bannu', 2026)
b1.data()