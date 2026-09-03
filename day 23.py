'''

                                    Regular Expressions (RegEx)
                                    ---------------------------
                                    ---------------------------

- this RegEx is used to form a searching pattern to find out the string contain sequence char or not
- to use this RegEx , we need to import re module

Functions
---------
---------
1. findall
----------
- the searching pattern is found, then it will gives the output in the list[] format

example:

import re
some = "python is a programming language"
print(re.findal("python", some))
------------------------------------------------------------------------------------------
2. search
- this is also used to form a search pattern, but it will give only the first matched
- where we will gives the index position, where the match objectmis found by the pattern

example:

import re
some = "python is a programming language"
print(re.search("[a]", some))
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

1.[]
----
- this [] symbol is used to find a group chat that present in the string, where we can also specify the range

syntax: re.findall('[range]', variable_name)

- by using this symbol we can search cap(A-Z), small(a-z) and digit(0-9)

example:

import re
some = "python is a programming language"
print(re.findall("aguo",some))
print(re.findall("a-z",some))
print(re.findall("A-Z",some))
print(re.findall("8-9",some))
print(re.search('[a-z]', some))

-----------------------------------------------------------------------------------------------------------

2. '.' char
-----------
- this symbol will refer only one means one match only single char in the pattern...
- one dot refers to one character

syntax - re.search('C...', variable_name)

example:

import re
some = 'Hello! World'
print(re.findall('H...o', some))
print(re.search('H...', some))
---------------------------------------------------------------------------------------------------------------

3. ^
-----
- ^ this symbol is used to find pattern where string starting match or not

syntax - re.findall('^', variable_name)

example:

import re
some = 'Hello! World'
print(re.search('^Hello', some))
print(re.findall('^Hello', some))
-----------------------------------------------------------------------------------------------------------------

4. $
----
- this $ symbol will find out if the string is ending with pattern or not

syntax - re.findall('sequence$', variable_name)

example:

import re
some = "I am planning for a trip"
print(re.findall('for a trip$', some))
print(re.search('for a trip$', some))
---------------------------------------------------------------------------------------------------------------

5. {}
-----
- the {} symbol is used to find group char that present in string

syntax - re.findall('E.{size}', variable_name)

example:

import re
some = "I have 1000 rupees with me"
print(re.findall('I.{2}', some))
--------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

import re
user_name = input("Please enter your name: ")
pattern = re.search('^[A-Z, a-z]{3,}', user_name)
if pattern:
    print('correct')
else:
    print('incoreect')
--------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------


import re
num = input("Enter a number: ")
f = re.findall('^[6-9][0-9]{9}$', num)
if f:
    print("Indian number")
else:
    print("Not indian number")
--------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
6. +
----
- the symbol max number of sequnce from the string from 

'''
