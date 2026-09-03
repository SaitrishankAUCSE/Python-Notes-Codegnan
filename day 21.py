'''
                                     super() method
                                     --------------
                                     --------------

-- this super() method is used to get the constructor from the parent and use in the child class
and also can get any method from the class...

class person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

class employee(person):
    def __init__(self, name, age, salary, role):
        super().__init__(name, age, role)
        self.salary = salary
        print("Employee Constructor called")

obj = employee("bannu", 21, 100, "Python Trainee")
print(obj.name)
print(obj.age)
print(obj.salary)
--------------------------------------------------------------------------------
class alls:
    def job(self):
        print("im looking for job")

class looking(alls):
    def job(self):
        super().job()
        print("We are looking for a candidate")

    def ans(self):
        super().job()
        print("no jobs")

anys = looking()
anys.ans()
------------------------------------------------------------------------------------

Polymorphism
------------
- polymorphism means a same name but different forms

types
-----
1. method overloading
--------------------
- this method overloading happening in class a method is created this time samenmaeo

example:

class data:
    def add_(self, a, b, c = 8):
        return a+b+c
    def add_(self,a,b,c):
        return a+b+c
    def add_(self, a,b,c,d):
        return a+b+c+d
obj = data()
print(obj.add_(1,2,3,5))
---------------------------------------------
2. mehtod overrriding
-------------------------
- this method overriding happend when parent class and child has same method and the child take its own implementation

example:

class pay:
    def payment(self):
        print("Payment failed")

class UPI(pay):
    def payment(self):
        print("UPI payment called")

class Paytm(pay):
    def payment(self):
        print("Paytm payment called")

obj = UPI()
obj.payment()

go = Paytm()
go.payment()
--------------------------------------------------------

3. operation overloading
------------------------
-- opearator overloading which gives specials meaning to the 
'''
class cal:
    def __init__(self, any_):
        self.any_ = any_
    def __add__(self, do):
        print(self.any_ * do.any_)

how = cal(7)
who = cal(10)
print(how+who)