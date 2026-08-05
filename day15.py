'''

                                                Modules
                                               ---------
                                               ---------
- Modules are the python code which is saved in (.py)....that contains functions, variables, classes, etc.

Types
-------
1. built-in : the built-in modules are already designed and comes with python, when python is installed in system

examples: math, sys, os, random, etc.
---------------------------------------------------------------------------------------------------------------------------
2.user-defined: the user-defined modules are created by the user or programmer

syntax - import(keyword) module_name
----------------------------------------------------------------------------------------------------------------------------
importing with alias name
------------------------
- we can also import a module with alias name, so that we can use the alias name instead of module name
- after importing with the alias name, we have to use that alias name in the code instead of module name, otherwise it will give error
----------------------------------------------------------------------------------
importing only needed function
------------------------------
- when we are importing the only needed few functionsfrom the modules, we can use the below syntax, so that we can use the function directly without using module name or alias name

syntax - from(keyword) module_name import(keyword) function_name
------------------------------------------------------------------------------
importing all functions from the module
---------------------------------
- when we are importing all the functions from the modules, we can use the below syntax, so that we can use the function directly without using module name or alias name

syntax - from(keyword) module_name import(keyword) *
---------------------------------------------------------

examples:

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b
---------------------------------------------------

def display(name):
    print(f' Welcome {name}')

display('Bannu')
---------------------------------------------------------
import random
ans = random.randint(1,10000000)
print(ans)
---------------------------------------------------
import math
print(math.sqrt(25))
'''