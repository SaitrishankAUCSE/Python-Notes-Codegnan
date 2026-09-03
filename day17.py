'''
                                                                 EXCEPTION HANDLING
                                                               ------------------------
                                                               ------------------------
- an error can be handled by try and except

1.try:
------
- The try block in Python is used for exception handling , which prevents your program from crashing when an unexpected runtime error occurs

syntax:
try:
    #write from here, take one tab space

example:
try:
    print(n)
except:
    print("error")
-------------------------------------------------------

2.except:
- The except block in Python is used to catch and handle exceptions that may occur in the try block. It allows you to define how your program should respond to specific errors, preventing it from crashing.
- exception can handle any error that come in the try block

syntax:
except:
    #write from here, take one tab space

example:1
try:
    num = 8
    num1 = 0
    print(num / num1)
except:
    print("will get an error because we are dividing a number by zero")


num = 8
num1 = 0
print(num / num1)

example:2
try:
    n = int(input("enter a number: "))
    print(n + 9)
except:
    print("error")

    
example:3
try:
    print("hii" + 9)
except:
    print("error")
-------------------------------------------------------------------------------------------------------------------------

3.else:
- The else block in Python is used in conjunction with the try and except blocks to define a block of code that should be executed if no exceptions occur in the try block. It allows you to specify actions that should be taken when the code runs successfully without any errors.
- if no error in the code is raised. then the else block will be executed

syntax:
else:
    #write from here, take one tab space

example:
try:
    print(4+5)
except:
    print("error")
else:
    print("no error in try block")

--------------------------------------------------------------------------------------------------------------------------
4.finally
- finally block in Python is used to define a block of code that will always be executed, regardless of whether an exception occurred or not. It is typically used for cleanup operations, such as closing files or releasing resources, ensuring that certain actions are performed even if an error occurs in the try block./
e- 

example:
try:
    print(hello)
except ZeroDivisionError:
    print("this will raise zero division error")
except NameError:
    print("this will raise name error")
except TypeError:
    print("this will raise type error")
else:
    print("no error in try block")
finally:
    print("this will always be executed")
................................................................................................................................................
------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                                              FILE HANDLING
                                             --------------
                                             --------------
                                        
- File handling in Python refers to the process of working with files, such as reading from and writing to files. Python provides built-in functions and methods to perform various file operations, making it easy to handle files in different formats.
- File handling allows you to create, open, read, write, and manipulate files on your computer's file system. It is an essential aspect of programming, enabling you to store and retrieve data persistently.
- In Python, you can work with different types of files, including text files, binary files, and CSV files. The most common file operations include opening a file, reading its contents, writing data to a file, and closing the file when you're done.
- Python provides a simple and intuitive way to handle files using the built-in open() function,
- which allows you to specify the file mode (read, write, append, etc.) and perform various operations on the file object returned by the function.
- an file handler is an object used to connect with that particular file....

1. with(keyword)
- 
example:
#by file name
with open('practice.py', 'r') as file:
    print(file.read())

example:
# by file path
with open(r'path', 'r') as file1:
    print(file1.read())

------------------------------------------------------------------------------------------------------------------------
2. open()
- open() is a built-in Python function used to open a file so that you can read, write, append, or create files.
- close() is a method used to close an opened file. It releases the system resources associated with the file and ensures that any changes are saved properly.

example:
ans = open('practice.py', 'r')
print(ans.read())
ans.close()
-------------------------------------------------------------------------------------------------------------------------

MODES
------
1. 'r'
- the 'r' mode is to read(), readLine() and readLines()

example:
with open('practice.py', 'r')as file:
    print(file.read())

2. 'w'
- the 'w' mode is used for writing or making changes in the file using write() function

example:
with open('demo.txt', 'w')as file:
    file.write("The tims is 13:14")
    print(file.write("\nThe tims is 13:868"))

3. 'a'
- the 'a' mode is used for write() function and it will add the text at last potition

example:
with open('demo.txt', 'a')as file:
    file.write("The tims is 13:14")
    print(file.write("\nThe tims is dwkjjdjs"))


4. 'x'
- it is used to create a file and paste data in it
- if no file exist with file name, while writing code, it will create a new file and paste that text in new file

example:
with open('demo1.txt', 'x')as file:
    file.write("The tims is 13:14")
    print(file.write("\nThe tims is dwkjjdjs"))

------------------------------------------------------------------------------------------------------------------------------------

FUNCTIONS
---------
1. write()

2. read() - it read all the data in the file, where we can specify the size- until where we want to read, like how many characters we want to read
- it read spaces also or count space as one character
example:
with open('demo.txt', 'r')as file:
    print(file.read(28))

3. readine() - it will read one line at a time

example:
with open('demo.txt', 'r')as file:
    print(file.readline())

4. readlines() it will read whole file and return it in a list format, where each line is one index in the list

example:
with open('demo.txt', 'r')as file:
    print(file.readlines())


'''
with open('demo.txt', 'r')as file:
    print(file.readline())
    print(file.readline())

