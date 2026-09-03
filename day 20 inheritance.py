'''
                                          INHERITANCE
                                          ------------
                                          ------------

- inheritance is the process of inherit once class into another class
- in general inherit from a class is called parent class and using it in another that class is called child class

example:

class company:
    def salary(self):
        print("Company salary")

class employee(company):
    def mon_salary(self):
        print("Employee salary")

per_sal = employee()
per_sal.mon_salary()
per_sal.salary()
--------------------------------------------------------------------------

TYPES
-----

1.single inheritance
--------------------
- this Single inheritance isan object-oriented programming concept where a derived (child) class inherits features, properties, and methods from only one base (parent) class

example:
class father:
    def land(self):
        print("5 acres of land")

class me(father):
    def flat(self):
        print('6 flat')

alls = me()
alls.flat()
alls.land()
-----------------------------------------------------------------------------

2.multiple inheritance
-----------------------
- if one child inherit from more than one parent class this is called multiple inheritance

example:
class father:
    def home(self):
        print("duplex house")

class mother:
    def gold(self):
        print("50kg gold")

class me(father, mother):
    def flat(self):
        print('sons flat')

alls = me()
alls.home()
alls.gold()
----------------------------------------------------------------------------------

3.multi-level inheritance
--------------------------
- it is process where one child class inherits properties and methods from two oe more parent classes

example:
class grandfather:
    def home(self):
        print("duplex house")

class father(grandfather):
    def flat(self):
        print("sons flat")

class son(father):
    
    def house(self):
        print('sons flat')

alls = son()
alls.home()
alls.flat()
alls.house()
-------------------------------------------------------------------------------

4.hierarchial inheritance
--------------------------
- it is the process where multuple child classes inherit from a single parent class

example:
class father:
    def land(self):
        print("50 acres land")

class son1(father):
    def flat(self):
        print("first sons flat")

class son2(father):
    def car(self):
        print('second sons car')

s1 = son1()
s1.land()
s1.flat()

s2 = son2()
s2.land()
s2.car()
--------------------------------------------------------------------------------------------------

5.hybrid inheritance
----------------------
- it is a combination two or more inheritances

example:
class student1:
    def name(self):
        print("His name is bannu")

class student1_study(student1):
    def study(self):
        print("B.Tech in andhra university")


class py_teacher:
    def python(self):
        print("He learns python")

class java_teacher:
    def java(self):
        print("He learns java")

class learner(py_teacher, java_teacher):
    def learns(self):
        print("he learns both python and java")

class all_get(student1_study, learner):
    def alls(self):
        print("Student3 learns from both students")


s3 = all_get()
s3.name()
s3.study()
s3.python()
s3.java()
s3.learns()
s3.alls()
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------
#single inheritance
'''
class mom:
    def quality(self):
        print("Mom has some qualities")

class son(mom):
    def son_quality(self):
        print("Son has same qualities as mom")

s1 = son()
s1.quality()
s1.son_quality()

#multiples inheritance
class mother:
    def hands(self):
        print("Mom has hands")

class father:
    def legs(self):
        print("Dad has legs")

class son(mother, father):
    def same(self):
        print("Son has similar hands of mother, and similar legs of father")

s = son()
s.hands()
s.legs()
s.same()

#multi-level inheritance
class grandfather:
    def hair(self):
        print("grand father has long har")

class father(grandfather):
    def hair_father(self):
        print("father has same long hair as grandfather")

class son(father):
    def hair_son(self):
        print("son has same hair as father and grandfather")

s = son()
s.hair()
s.hair_father()
s.hair_son()

#hierarchial inheritance

class car:
    def attributes(self):
        print("Every car has doors and wheels")

class audi(car):
    def audi_attributes(self):
        print("Audi car also have doors and wheels")

class benz(car):
    def benz_attributes(self):
        print("Benz car also have doors and wheels")

a1 = audi()
a1.attributes()
a1.audi_attributes()

b1 = benz()
b1.attributes()
b1.benz_attributes()
'''
#5 hybrid inheritance

class amazon:
    def work(self):
        print("He has worked in amazon")

class amazon_salary(amazon):
    def salary(self):
        print("His salary in amazon is 5LPA")


class zoho:
    def worked(self):
        print("After amazon he joined zoho")

class zoho_salary(zoho):
    def zoho_sal(self):
        print("His salary in zoho is 12LPA")


class all_get(amazon_salary, zoho_salary):
    def answer(self):
        print("He has experience in both amazon and zoho companies")


a = all_get()
a.salary()
a.zoho_sal()
a.answer()