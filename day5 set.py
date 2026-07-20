'''
                      Set
                    -------

- set is an unordered collection
- set do not allow duplicate values inside it
- set is mutable
- set is represented in {}
----------------------------
example:
do = {1,2,3,2}
print(do)

#creating an empty set
so = set()
print(type(so))
--------------------------------------

Methods:
---------
---------
1.update
- use to update or add new values into set

syntax -- variable_name.update(iterable)

example:
do = {1,2,3,2}
do.update("PYTHON")
print(do)
---------------------------------------

2.add:
- use to add new value into set

syntax -- variable_name.add(iterable)

example:
do = {1,2,3,2}
do.add("PYTHON")
print(do)
------------------------------------------

3.remove()
- use to remove or delete values from set, if the value is not present in the set, it will throw the KeyError

syntax -- variable_name.remove(iterable)

example:
do = {1,2,3,2}
do.remove(2)
print(do)
----------------------------------------------

4.discard()
- used to del the value from the set, but it does not throw any error if a value is not present in set

syntax -- variable_name.discard(iterable)

example:
do = {1,2,2,1,3,2}
do.discard(8)
print(do)
------------------------------------------------

5.pop()
- used to pop or delete the first indexed value, and it does not take any arguments, i.e. it does not allow index deletion, it only deletes first element in set

syntax -- variable_name.pop()

example:
do = {1,2,3,4,5,6}
do.pop()
print(do)


Operations
-----------
-----------
1.union
- combines values of both sets into one set and does not allow duplicates

syntax -- print(varibale_name1 | variable_name2)    or    print(varibale_name1.union(variable_name2))

example:
do = {1,2,3}
so = {3,4,5}
print(do&so)#or
print(do.intersection(so))
-------------------------

2. intersection
- returns all common values present in both sets

syntax -- variable_name1&variable_name2   or    variable_name1.intersection(variable_name2))

example:
do = {1,2,3}
so = {3,4,5}
print(do&so)#or
print(do.intersection(so))
-----------------------------

3.difference
- returns all non common values of a set,  if variable1 - variable2 ==> finds differnce from set1    or    if variable2 - variable1 ==> finds differnce from set2

syntax -- variable_name1-variable_name2   or    variable_name1.difference(variable_name2))

example:
do = {1,2,3}
so = {3,4,5}
print(so-do)#or
print(so.difference(do))
----------------------------------------------------------------------------------
------------------------------------------------------------------------------------

                           Type Conversions
                        ----------------------

Int:
------------------
------------------
Integer -- str():

example:
num = 9
print(type(num))
so = str(num)
print(so)
print(type(so))
-------------------

Integer -- float():

example:
num = 9
print(type(num))
so = float(num)
print(so)
print(type(so))
-------------------

Float:
---------------
---------------
Float to str():
num = 8.67
print(num)
print(type(num))
so = str(num)
print(so)
---------------
Float to int():
example:

num = 8.67
print(num)
print(type(num))
do = int(num)
print(do)
print(type(do))
-----------------

String
-----------
-----------
String to int():
- this caanot be done, because it raises an error
for example:
so = " i have 69 rupees"
print(type(so))
do = int(so)
print(type(do))

- this can be done
for example:
so = "100"
print(type(so))
do = int(so)
print(do)
print(type(do))
------------------
String to float():
example:
so = "100"
print(type(so))
do = float(so)
print(do)
print(type(do))
------------------
String to list:
example:
so = "1,2,3,4"
print(so)
print(type(so))
do = list(so)
print(do)
print(type(do))
-----------------
String to tuple:
example:
so = "1,2,3,4"
print(so)
print(type(so))
do = tuple(so)
print(do)
print(type(do))
-----------------


List
-------
-------
List to str():
example:
nums = [1,2,3,4]
print(nums)
print(type(nums))
numso = str(nums)
print(numso)
print(type(numso))
-------------------

List to tuple:
example:
nums = [1,2,3,4]
print(nums)
print(type(nums))
numso = tuple(nums)
print(numso)
print(type(numso))
--------------------


Tuple
------
------
Tuple to list:
example:
nums = (1,2,3,4)
print(nums)
print(type(nums))
numso = list(nums)
print(numso)
print(type(numso))
------------------

Tuple to str():
example:
nums = (1,2,3,4)
print(nums)
print(type(nums))
numso = list(nums)
print(numso)
print(type(numso))
-------------------



                    Concatenation
                ---------------------

(+)
examples:
#numbers
num1 = 8
num2 = 9
print(num1 + num2)

#characters or words
ch1 = "Python is a "
ch2 = "Language"
print(ch1 + ch2)

#list
l1 = [1,2]
l2 = [3,4]
print(l1 + l2)

#tuple
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)
'''
#numbers
num1 = 8
num2 = 9
print(num1 + num2)

#characters or words
ch1 = "Python is a "
ch2 = "Language"
print(ch1 + ch2)

#list
l1 = [1,2]
l2 = [3,4]
print(l1 + l2)

#tuple
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)

