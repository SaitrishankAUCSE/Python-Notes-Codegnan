'''
scenario to understand(*args and **kwargs)
modules --> some interesting cases -> projects(virtual assistant, email automation)
oop -> github(branch)
--------------------------------------------------------------------------------------------
#employee 
def employees(*names,**settings):
    """employee details along with their settings"""
    print("Employee Names")
    for employee in names:
        print('---------------------')
        print('-', employee)

    for key, value in settings.items():
        print("\nKey: ", key)
        print("Value: ", value)

#if __name__ == "__main__":

details = {'organization' : 'codegnan',
                'year' : 2018,
                'branches' : ['vijayawada','hyderabad', 'vizag']}

print(__name__)  #dunder methods --> magic methods
--------------------------------------------------------------------------------------------
----------this code must be done in another file
--------------------------------------------------------------------------------------
import day4
print(dir(day4)) #dir --> directory will return all avialable methods, attributes
print(type(day4.details))
print(type(day4.employees))

day4.employees("bannu", designation = "co-founder",location = "vizag")

print(day4.details.items())
print(day4.details['branches'])
day4.details.update({'batches' : ['pfs5', 'jfs5', 'da', 'aaa', 'ds'], 'employees' : 240})
print(day4.details)


#from keyword
import day3
import day4
from day4 import employees, details
print(details)
details.update({'batches' : ['pfs5', 'jfs5', 'da', 'aaa', 'ds'], 'employees' : 240})
print(details)
print(day3.__doc__)

'''
#built-in modules --> math, os, random, time, datetime
#we download modules --> pypi (python package index)

#build a QRcode scanner using python --> linkedin URL
#we use pyqrcode module, and save in image(png,jpeg) format
#we use module pypng
#pip install pyqrcode
#pip install pypng


import pyqrcode
import png

#create a qrcode by giving a link
link = "www.linkedin.com/in/saitrishank"
qr = pyqrcode.create(link)
print(qr)
qr.png("myqr.png", scale = 10)































