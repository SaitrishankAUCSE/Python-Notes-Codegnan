'''
Python Project --> POP/OOP
POP (Procedure Oriented Programming) --> Dividing the entire code into blocks --> procedure -> function (def)

FUCNTIONS -> A reusable block of code --> A block of statements which performs a specific tasks)
syntax :
def <function_name>(parameters):
        """doc string"""
        statement(s)...


#simple scenario to understand
def add(a,b):
    """Addition Function"""
    c = a+b
    return c
print(add(3,5))
c,d = 'codegnan','bannu'
print(add(c,d))  #concatenation
e,f = map(str, input("Enter the values: ").split(','))
print(add(e,f))
print(add[1,2,3],[4,5,6]) #merging



#variable length arguments -> *args we can any number of positional argumnts --> data will be stored in tuple...
def sample(*a):
    """Demo of variable length arguments"""
    print(a)
    print(type(a)) #default it stores in tuple fomat
sample()
sample(2,3,4,5)
sample('codegnan',[23,4],'poll',2+5j)

marks = [20,13,25,18]
sample(marks)
sample(*marks)
a,b,*c = 12,'code','poll',23,4,9
print(a)
print(b)
print(c)


def add(*a):
    """perform addition for numeric values"""
    print(a)
    result = 0
    for i in a:
        if type(i) in [int, float]: 
        #print(i)
            result = result + i
    return result
print(add(2,3,4))
print(add(2,'codegnan',3,4))


def batch(name, age, place='vizag'):    
    def batch(name = 'bannu', age, place = 'hyd'): #error -> non default always follows
    """keyword arguments usage"""
        print(f'{name} is in {place} and age is {age} years')
batch('codegnan', 18, 'vizag')
batch(age = 18, name='codegnan')
#keyword arguments only needs name matching not order

batch(age = 21, place =' hyd', name = 'bannusai')
#default arguments can accept a value as default


print(4,5)
print(4,5, sep=':') #here keyword argument is sep and we are changing the default value for sep




#keyword variable lenght arguments (**kwargs) --> any number of keyword arguments, data is stored in dictionary


def batch(**a):
    """keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name = "bannu", age = 21, place = 'vizag', branch ='cse')

data = {'names' : ['akash', 'praneeth'],
             'places' : ['vizag', 'hyderabad']}
batch(**data)
data.update({'batch':'pdf-vsp-007'})
batch(**data)
'''
#task : create a function with the usage of *args & **args
def employer(*name, **age, empid, salary, role):
    print(*name)
    print(**age)

empid, salary, role, *name, **age = 111, 100000, HR, 'bannusai', 'sai trishank', 22
print(empid)
print(salary)
print(role)














    
