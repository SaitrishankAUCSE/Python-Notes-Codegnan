'''
               default arguments
               --------------------
               --------------------
example:
def any(name, age, education):
    print(age)

any('bannu',87, 'cse')
----------------------------------
def any(name, age, education):
    print(age)
    print(name)

any(name = 'bannu',age = 87, education = 'cse') 
-----------------------------------------------
-----------------------------------------------

Variable length positional arguments
---------------------------------------
*args
------
- we can pass tuple of arguments and store in a parameter by just adding * before the parameter...
- and we can access the arguments using indexing

example:

def all_val(*nums):
    print(nums[1] + nums[3])
all_val(10, 34, 5, 89)
--------------------------------

Variable- length keyword arguments
---------------------------------------
**kargs
--------
- By pass keyword in the arguments, will get it as dictionary
- and can access by using dictionary methods...

example:

def dicts(**allin):
    for key, val in allin.items():
        print(key, '=' , val)
dicts(name = 'bannu', age = 21, role = ' trainee')

example:2

def dict_nums(*args, **kargs):
    print(args)
    print(kargs)
dict_nums(12, 56, 7, name = 'bannu', age = 21, edu = 'B.Tech')
--------------------------------------------------------------
num2 = 21
def num1(num2):
    num = 90
    print(num)
    print(num2)
num1(num2)
print(num2)
-----------------------------------------------------------------

limit = int(input("Enter limit: "))
num1 = 0
num2 = 1
def fibonacci(limit, num1, num2):
    print(num1, num2, end = ' ')
    for i in range(1, limit+1):
        total = num1 + num2
        num1 = num2
        num2 = total
        print(total, end = ' ')

fibonacci(limit, num1, num2)
-----------------------------------------------------------------------
-----------------------------------------------------------------------

Passing by values
-------------------
- passing direct values in the arguments
example:

def any(a,b):
    print(a)
    print(b)
any(8,56)
---------------------------------------------
'''
def any(num1, num2):
    print(num1)
    print(num2)
any(num1 = int(input("enter a num: ")), num2 = int(input("enter another number: ")))
