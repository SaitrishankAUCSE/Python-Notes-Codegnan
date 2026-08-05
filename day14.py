'''

                                 List comprehension
                                 ---------------------
                                 ---------------------

- the comprehension is the short form of syntax used to generate a new list from the old list

syntax - [expression loop]

example:
nums = [1,2,3,4,5]
new1 = [i for i in nums]
new2 = [i for i in nums if i%2==0 else 'odd']
new3 = [i if i%2==0 else 'odd' for i in nums] # if we want to use else condition after if condition, we have to use for loop after the if and else conditions only
print(new1)
print(new2)
print(new3)
-------------------------------------------------------------------

Nested Comprehension
-------------------------
- nested comprehension means an comprehension inside the another comprehension

syntax - [expression loop1 and loop2]

example:
match = [[1,2,3],[4,5,6],[7,8,9]]
alls1 = [i for i in match]
alls2 = [num for j in match for num in j] # num means individual list or [1,2,3]...so "j in match" means one list in match......and "for num in j" means individual num in j means - individual letter print
print(alls1)
print(alls2)
---------------------

new = [[i*j for i in range(1,5)] for j in range(1,5)]
news = [i for i in range(1,5)]
print(new)
print(news)
---------------------------------------------------------------------------------------------

Generator
----------

-this generator will generate value one at a time and the pause it on th  position when we are using yield keyword.
- here we will use yield to get the value

yield Keyword
---------------
- this yeild() keyword is used to get the value and will only gives one value and pauses there itself

next keyword
--------------
- the next() will retrieve the value

example:

def nums(n):
    for i in range(1, n+1):
        yield i*i
a = nums(5)
print(next(a))
print(next(a))
---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------

Function
---------
- return
- when the return is executed, it will exit from the function
- in functions we will get all values once(like when we execute return function, we will get all values)

Generator
----------
- yield
- when the yield is executed, it will pause the function and the next yield is called, the function will resume again
- in generator we will get one value at a time
'''
