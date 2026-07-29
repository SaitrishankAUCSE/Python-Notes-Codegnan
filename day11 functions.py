'''
                               Functions
                               ----------
                               ----------

- function is a block of code that can be executed when we call it...
- to avoid the repeated lines of code...
syntax -
def function_name(parameters):
   -------
   -------
   -------
function_name(arguments)



Types of fucntions:
-------------------------
1. Built-in fucntions (len(), print(), max(), min())
2. User defined functions (these functions are developed and run by users)

example:
def fucntion for adding two numbers:
def total(num1, num2):
    print(num1 + num2)
total(10, 20)
total(60, 50)
------------------------------------
def function for subtracting two number:
def total(num1, num2):
    print(num1 - num2)
total(10, 20)
total(60, 50)
-------------------------------------
def function for remianing operators:
def total(num1, num2):
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
total(10, 20)
total(60, 50)
------------------------------------------
--------------------------------------------


required argument
---------------------
- we have to pass same number of arguments that match with parameters. the parameters and arguments must be of same length.
example:

num1 = 56
num2 = 89

def total(num1, num2):
    print(num1)

total(num1, num2)
total(1, 2, 3)
-------------------------------------
def name(name, name_):
    print(name)
    print(name_)

name(name = 'Bannu', name_ = 'Sai')
--------------------------------------
def name(name1, name2, name3, name4, name5):
    print(name1)
    print(name2)
    print(name3)
    print(name4)
    print(name5)

name(name1 = 89, name3 = 'hii', name4 = 10000, name2 = 'Bannu', name5 = 'Sai')
------------------------------------------------------------------------------------
'''
def name(name1, name2, name3, name4, name5):
    print(name1)
    print(name2)
    print(name3)
    print(name4)
    print(name5)

name(name1 = 89, name3 = 'hii', name4 = 10000, name2 = 'Bannu', name5 = 'Sai')
