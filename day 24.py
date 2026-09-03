'''

                                          DATA ANALYSIS
                                          -------------
                                          -------------

- Data analysis is the process of collecting, cleaning, transforming, organizing, and analyzing data to convert it into useful information and support better decision-making.

libraries
---------
1. NumPy
--------
- this refers to numerical python
- it is a python library used for calculations and operations

example:

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.ndim)


Functions
---------
ndim
----
- this function is used to find out the dimensions of an array

syntax - array.ndim

example:

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.ndim)
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.ndim)


shape
-----
- this shape function is used to find the row & col of an array

syntax - array.shape

example:

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.shape)

reshape
-------
- this function is used to convert one dimension to another if the elements are there convert into any dimesnion
example:

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))


size
-----
- this size function is used to find out the number of elements present in an array

syntax - array.size

example:

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.size)

operations
----------
- same as list we can perform operations on arrays
1.indexing:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[2])

2.slicing
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[2:5])

3.sum:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.sum())

4.add:
import numpy as np
arr = np.array([1,2,3,4,5,6])
arrs = np.array([1,2,3,4,5,6])
print(arr + arrs)
print(arr + 5)

5.sub:
import numpy as np
arr = np.array([1,2,3,4,5,6])
arrs = np.array([1,2,3,4,5,6])
print(arr - arrs)
print(arr - 5)

6.mul:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr * 5)

7.pow:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr ** 2)

8.div:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr / 2)

8.max:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.max())

9.min:
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.min())

10.range:
import numpy as np
arr = np.arange(10)
print(arr)

11.arange:
- the arange function is used to generate number in a sequence up to certain limit and it forms 1 dimensional array
- this array can convert into 2D arrays by using reshape

syntax - np.arange(range)

example:
import numpy as np
arr = np.arange(1,10)
print(arr.reshape(3,3))
print(arr)

---------------------------------------------------------------
2. Pandas
3. matplotlib
4. seaborn           

'''
import numpy as np
arr = np.arange(1,10)
print(arr.reshape(3,3))
print(arr)
