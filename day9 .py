'''
Program : To print numbers for a certain range and printing if they are odd or even

num = int(input("Enter the Range of numbers: "))
for i in range(1, num+1):
    if i %2 == 0:
        print(f' {i} is Even Number')
-------------------------------------------------------------------------------------------
Program: To check if a number is prime number or not

num = int(input("Enter a number: "))
count  = 0
for i in range(1, num+1):
    if num%i == 0:
        count += 1
if count == 2:
    print(f' {num} is a prime number')
else:
    print(f' {num} is not a prime number')
------------------------------------------------------------------------------------------
Program: To print prime number in a certain range of numbers

num = int(input("Enter range: "))
for i in range(2, num):
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(f' {i} is prime number')
    else:
        print(f' {i} is not prime number')
------------------------------------------------------------------------------------------
program: to check given string is palindrome or not using for loop

ch = input("Enter a string: ")
emp = " "
for i in ch:
    emp = i + emp
if  ch == emp:
    print(f' {ch} is a palindrome')
else:
    print(f' {ch} is not a palindrome')
---------------------------------------------------------------------------------------------------
program: to print stars or numbers
num = int(input("Enter a number: "))
count  = 0
for i in range(num+1, 0, -1):
    for j in range(1, i+1):
        print('*', end = ' ')
    print()
------------------------------------------------------------------------------------------------------
program:
num = int(input()) #20
for i in range(num, 0, -1):
    print(" " * (num - i -1), end = ' ')
    print('@' * (i+1))
-------------------------------------------------------------------------------------------------
program: remove duplicates in a list:
nums = list(map(int, input('Enter elements: ').split()))
emp = [ ]
for i in nums:
    if i not in emp:
        emp.append(i)
print(emp)
----------------------------------------------------------------------------------------------------------

program: to check if a number is perfect number or not
nums = int(input("Enter number: "))
per = 0
for i in range(1, nums):
    if nums % i == 0:
        per += i
if per == nums:
    print(f' {nums} is perfect number')
else:
     print(f' {nums} is not a perfect number')
