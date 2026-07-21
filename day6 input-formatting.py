'''
                     Input Formatting
                    ---------------------

int
----
example:
num = int(input("enter a number:"))
print(num+9)
print(type(num))
-------------------------------------------

string
-------
example:
string = input("enter a string:")
print(string+"hii")
print(type(string))
-----------------------------------------------

list
----
- for list and tuples, we use "map" named keyword
example:for numbers
lists = list(map(int,input("Enter numbers: ").split()))
print(lists)
print(type(lists))

example: for only strings
lists = input("Enter string: ").split()
print(lists)
print(type(lists))
-------------------------------------------------

tuple
------
example:for numbers
tup = tuple(map(int,input("Enter numbers:").split()))
print(tup)
print(type(tup))

exmaple:for strings
tup = tuple(input("Enter strings:").split())
print(tup)
print(type(tup))



EVAL FUNCTION
----------------------

nums  = eval(input("Enter value:"))
print(nums)
print(type(nums))

----------------------------------------
--------------------------------------
REVERSE A STRING:
nums = input("Enter string: ")
print(nums[::-1])

------------------------------------------

24 HOUR CLOCK TO 12 HOUR CLOCK:
times = input("Enter time in 24 hours: ")
parts = times.split(':')
hours = int(parts[0]) - 12
print(hours, ":", parts[1], "PM")
---------------------------------------------

12 HOUR CLOCK TO 24 HOUR CLOCK:
times = input("Enter time in 12 HOURS: ")    # taking time as input, using int and input functions
p = times.split(":")                                       # splitting the input time(taken from input), using split() function and by ':'
hours = int(p[0]) + 12                                  # this is the main function to convert the inputted time into 24 hours time, by adding 12 to only hours, without touching minutes
print(hours, ":", p[1], "PM")                          # print in a sequence ot output - hours(calculated in above function) , apply semi colon, print minutes, and PM +
'''
