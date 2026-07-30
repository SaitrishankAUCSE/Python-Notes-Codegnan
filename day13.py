'''

      ANONYMOUS FUNCTION OR LAMBDA FUNCTION
      --------------------------------------------------
      --------------------------------------------------

- anonymous function is a function, which dont have any name and keyword used is "lambda"
- this is also called as lambda function
- lambda function will take n number arguments but only one expression

syntax -
lambda arguments : expression

example:

so = lambda a, b, c,d  : a + b + c + d
print(so(2,5,3, 6))
------------------------------------

map()
------
- the map function will be applied on the given fucntion of each and every element of an iterbale

example:

nums = [1,2,3,4,5]
so = list(map(lambda x : x*x, nums))
print(so)
-------------------------------------------------------------------------------------------

filter()
--------
- filter() function will only consider if the condition is true, then it will keep that values...

example:

nums = [1,2,3,4,5]

so = list(filter(lambda x : x%2==0, nums))
print(so)
-------------------------------------------------------------------------

reduce()
---------
- the reduce() function consider all elements and reduce to one single value...
- to use this function we have to import it from functools

syntax -
from functools import reduce

example:

from functools import reduce
nums = [1,2,3,4,5]

so = reduce(lambda x, y : x+y, nums)
print(so)
-------------------------------------------------------------------------

print() vs return:
-----------------
- print() is an in built or built-in function that is used to display the value or output, stored by variable...
- return only used inside the functions(user defined or built-in). When the return is executed then it will exit from that function and holds the returned values and prints only when the print function is called.
