'''
                                    MODULES TYPES
                                    ------------------
                                    ------------------

math
------
------
- math module is used to do work on mathematical functionalities

TYPES:
-------

1.floor
- it will round-down to the near value
example:
import math
print(math.floor(5.87))

2.ceil
- it will round-up to the near value
example:
import math
print(math.ceil(5.87))

3. gcd
- it will find the gcd(greatest common divisor) value
example:
import math
print(math.gcd(24,36))

4.LCM
- it will find the lcm value
example:
import math
print(math.lcm(2,4,6))

5.sqrt
- it will give the square root value
example:
import math
print(math.sqrt(25))

5.factorial
- it will give the factorial value
example:
import math
print(math.factorial(5))

6. log
- it give log value of a number
example:
import math
print(math.log(2, 3))

7. cos
- it give cos value of a number
example:
import math
print(math.cos(math.pi))
--------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------

Random
--------
--------
- the random module is used to get the random value or random number

TYPES:
--------
1.randint
- it generates random numbers or value within the range
example:
import random
print(random.randint(1,100))

2. choice
- it will pick the random value from the given data
example:
import random
color = ['red', 'green', 'blue']
print(random.choice(color))

3. shuffle
- it will shuffle the data randomly
example:
import random
color = ['red', 'green', 'blue']
random.shuffle(color)
print(color)

4.uniform
- it will print decimal values in a range  given
example:
import random
print(random.uniform(99, 100))
-------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------

Sys
-----
-----
- sys module is used to get details of python interpreter

TYPES:
-------
1. version
- it will give the version of python interpreter
example:
import sys
print(sys.version)

2.path
- it will give all the .py paths 
example:
import sys
print(sys.path)

3. exit
- this function is used to exit from the program
example:
import sys
print(sys.exit())

4.platform
- it will give the platform name on which python is running in our system
example:
import sys
print(sys.platform)



import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())
print(platform.release())

5. argv
- it will give the curent file name, which you are using
example:
import sys
print(sys.argv)
-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

Date Time
----------
----------
- used to work with date and time

TYPES:
-------
1. now
- it will give the today time + date
example:
from datetime import datetime
print(datetime.now())

CODE:
from datetime import datetime
now = datetime.now()
print(now.strftime('%Y-%m-%d'))
print(now.strftime('%A'))
print(now.strftime('%B'))
print(now.strftime('%H:%M:%S'))
-------------------------------------------------

%Y -- year
%m -- month
%d -- day
%H -- hour
%M -- minute
%S -- second
%A -- current day
%B -- current month
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
Collections
------------
------------
- The collections module provides alternative data types to the built-in Python data types, which is more powerfull than built-in data types(dict, list, tuple, set)

1.Counter 
- it returns the count of each element in the given data in dictionary format
example:
import collections
data = ['apple', 'banana', 'orange', 'pineapple', 'banana']
print(collections.Counter(data))

2. deque
2(i) append and appendleft
- it is a double ended queue, which allows you to add or remove elements from both ends
example:
from collections import deque
data = deque([1,2,3,4,5])
data.append(6)
print(data)
data.appendleft(6)
print(data)

2(ii) extend and extendleft
- it is used to add multiple elements in the deque
example:
data = deque([1,2,3,4,5])
data.extend([6,7,8])
print(data)
data.extendleft([6,7,8])
print(data)

2(iii) pop and popleft
- it is used to remove elements from the deque
example:
from collections import deque
data = deque([1,2,3,4,5])
data.pop()
print(data)
data.popleft()
print(data)

3. namedtuple
- it is used to create a tuple with named fields, which allows you to access the elements of the tuple using dot notation instead of index
example:
from collections import namedtuple
data = namedtuple("stu", ('name', 'age'))
print(data('john', '21'))
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

itertools
----------
----------
TYPES:
1. count
- it is used to generate an infinite sequence of numbers, starting from a given number and incrementing by a given step
example:
from itertools import count
c = count(100)
for i in range(5):
    print(next(c))

2. repeat
- it is used to generate an infinite sequence of a given value, repeating it a given number of times
example:
import itertools
for i in itertools.repeat('Python', 10):
    print(i)

3. permutations
- it is used to generate all possible permutations of a given iterable, with a given length
example:
from itertools import permutations
data = permutations([1,2,3], 2)
print(list(data))

4. combinations
- it is used to generate all possible combinations of a given iterable, with a given length
example:
from itertools import combinations
data = combinations([1,2,3], 2)
print(list(data))
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

06-08-2026
-------------
practice on modules
----------------------
import random
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
# ascii_letters -> this string module function can give alphabets from a-z and A-Z
# digits --> string module function that can give numbers from 0-9
#npunctuation --> this tring module function can give us special characters like (!@#$%^&*)
------------------------------------------------------------------------------------------------

#To generate password with mix of digits, special characters, letters:

import random
import string

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all = letters + digits + punctuation
password = ""
for i in range(5):
    password += random.choice(all)
print(password)
------------------------------------------------------------------------------------------------

import random
import string

letters = string.ascii_letters
digits = string.digits
special = '@#*$'

all = letters + digits + special
password = ""
for i in range(5):
    password += random.choice(all)
print(password)
----------------------------------------------------------------------------------------------------------
balance = 10000
from datetime import datetime
import sys
now = datetime.now()

while True:
    print("----Welcome to SBI ATM---")
    user_otp = int(input("\n1.Withdraw \n2.Deposit \n3.Check Balance"))
    if user_otp == 1:
        withdraw_money = int(input("Enter the money you want to withdraw: "))
        if withdraw_money > balance:
            balance -= withdraw_money
            print(f'Remaining money {balance} {now.strftime("%H:%M %Y-%m-%d")}')
        else:
            print('insufficient money')
    elif user_otp == 2:
        deposit_money = int(input("Enter the money you want to depsoit: "))
        balance += deposit_money
        print(f'Money deposited successfully : {balance} {now.strftime("%H:%M %Y-%m-%d")}')
    elif user_otp == 3:
        print(f'Available balance: {balance} {{now.strftime("%H:%M %Y-%m-%d")}}')

    elif user_otp == 4:
        sys.exit()
    else:
        print("Incorrect choice")
        print("Thanks for visiting the ATM")
        sys.exit()
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
#Number Guessing game
import random
print("Hi Player! \nWelcome to Number Guessing Game")
name = input("\nPlease enter your name: ")
print(f'\nHi {name}, Lets start the Game!')
score = 0

randnumber = random.randint(1,5)
print(randnumber)
number = int(input("Enter a number between 1 to 5: "))
if randnumber == number:
    score += 10
    print(f'Hurray! Your guess was correct!!! \nYour score is {score}')
    
if randnumber != number:
    score -= 2
    print(f'OOPS! {name}, Your guess was wrong \nBetter luck next time!!!')
    
