'''
             Tuple
            --------

- tuple is collection of different data types that are represented in () and separated by ,
- tuples are immutable

example:
gom = (1, 'java', [3,4], ('python', 78)) 
print(gom.count(('python', 78))) --- o/p - 1
print(gom.count('python'))    ---- o/p - 0
----------------------------------------------------
---------------------------------------------------


            Dictionary
          -------------
- dict is a keyvalue pair
- keys and values separated by :
- dict is represented by []
--------------------------------------
example:
man = {1:9,
       'name' : 'bannu',
       (6,7) : 90,
       2:90,
       'age': 21,
       'gender' : 'males'}
print(man)


example:
bank_details = {'name' : 'Bannu',
                'account-no' : 8492842342,
                'IFSC code' : 'SBIN193849U',
                'pin' : 2101}
print(bank_details)
----------------------------------------------
METHODS
1.Keys
------
syntax - dict.keys()

2.values
---------
syntax - dict.values()

3.items
--------
syntax - dict.items()
---------------------------
example:
bank_details = {'name' : 'Bannu',
                'account-no' : 8492842342,
                'IFSC code' : 'SBIN193849U',
                'pin' : 2101}
print(bank_details)
print(bank_details.keys())
print(bank_details.values())
print(bank_details.items())
------------------------------------------

4.update
--------
syntax - dict.update({key:value})

example:
bank = {'name' : 'Bannu',
                'account-no' : 8492842342,
                'IFSC code' : 'SBIN193849U',
                'pin' : 2101}
bank.update({'name':'sai'})
print(bank)
-----------------------------------------------
5.clear()
------------
syntax - dict.clear()

'''

bank = {'name' : 'Bannu',
                'account-no' : 8492842342,
                'IFSC code' : 'SBIN193849U',
                'pin' : 2101}
bank.clear()
print(bank)
