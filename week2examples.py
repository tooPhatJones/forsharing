
# the range() function{{{
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)
# 0
# 1
# 2
# 3
# 4
# 5
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)
# 2
# 3
# 4
# 5

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29
# }}}
# For Loops{{{
# https://www.w3schools.com/python/python_for_loops.asp
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# apple
# banana
# cherry
# The for loop does not require an indexing variable to set beforehand.

# Looping Through a String
for x in "banana":
  print(x)
# b
# a
# n
# a
# n
# a

# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# apple
# banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# apple

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# apple
# cherry

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)
# 0
# 1
# 2
# 3
# 4
# 5
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)
# 2
# 3
# 4
# 5
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
  print(x)
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# 0
# 1
# 2


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement#}}}
















# Python Functions{{{
# a function is a reusable block of code
def my_function():
  print("Hello from a function")
my_function() # Hello from a function
# passing arguments{{{
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

# error with incorrect number of args
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil") #error
# Traceback (most recent call last):
  # File "demo_function_args_error.py", line 4, in <module>
    # my_function("Emil")
# TypeError: my_function() missing 1 required positional argument: 'lname'


#if you pass the incorrect number of arguemnts, you will get an error
def my_function(fname, test):
  print(fname + " Refsnes")

my_function("Emil")
# Traceback (most recent call
# last):
  # File "forExecution.py", li
# ne 4, in <module>
    # my_function("Emil")
# TypeError: my_function() tak
# es exactly 2 arguments (1 gi
# ven)
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil", 'test')
# Traceback (most recent call
# last):
  # File "forExecution.py", li
# ne 8, in <module>
    # my_function("Emil", 'tes
# t')
# TypeError: my_function() tak
# es exactly 1 argument (2 giv
# en)

# #}}}
# Return Values{{{
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# 15
# 25
# 45

# The return keyword is to exit a function and return a value.
def myfunction():
  return 3+3
print(myfunction())
# 6
# you dont have to use the returned value
def myfunction():
  return 3+3
  print '4' # orphaned code, wont run, no errors
myfunction()
# nothing happens



# #}}}
# #}}}
# Python Built in functions**{{{

# * abs()	Returns the absolute value of a number
# * all()	Returns True if all items in an iterable object are true
# * any()	Returns True if any item in an iterable object is true
# * ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# * bin()	Returns the binary version of a number
# * bool()	Returns the boolean value of the specified object
# * bytearray()	Returns an array of bytes
# * bytes()	Returns a bytes object
# * callable()	Returns True if the specified object is callable, otherwise False
# * chr()	Returns a character from the specified Unicode code.
# * classmethod()	Converts a method into a class method
# * compile()	Returns the specified source as an object, ready to be executed
# * complex()	Returns a complex number
# * delattr()	Deletes the specified attribute (property or method) from the specified object
# * dict()	Returns a dictionary (Array)
# * dir()	Returns a list of the specified object's properties and methods
# * divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# * enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# * eval()	Evaluates and executes an expression
# * exec()	Executes the specified code (or object)
# * filter()	Use a filter function to exclude items in an iterable object
# * float()	Returns a floating point number
# * format()	Formats a specified value
# * frozenset()	Returns a frozenset object
# * getattr()	Returns the value of the specified attribute (property or method)
# * globals()	Returns the current global symbol table as a dictionary
# * hasattr()	Returns True if the specified object has the specified attribute (property/method)
# * hash()	Returns the hash value of a specified object
# * help()	Executes the built-in help system
# * hex()	Converts a number into a hexadecimal value
# * id()	Returns the id of an object
# * input()	Allowing user input
# * int()	Returns an integer number
# * isinstance()	Returns True if a specified object is an instance of a specified object
# * issubclass()	Returns True if a specified class is a subclass of a specified object
# * iter()	Returns an iterator object
# * len()	Returns the length of an object
# * list()	Returns a list
# * locals()	Returns an updated dictionary of the current local symbol table
# * map()	Returns the specified iterator with the specified function applied to each item
# * max()	Returns the largest item in an iterable
# * memoryview()	Returns a memory view object
# * min()	Returns the smallest item in an iterable
# * next()	Returns the next item in an iterable
# * object()	Returns a new object
# * oct()	Converts a number into an octal
# * open()	Opens a file and returns a file object
# * ord()	Convert an integer representing the Unicode of the specified character
# * pow()	Returns the value of x to the power of y
# * print()	Prints to the standard output device
# * property()	Gets, sets, deletes a property
# * range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# * repr()	Returns a readable version of an object
# * reversed()	Returns a reversed iterator
# * round()	Rounds a numbers
# * set()	Returns a new set object
# * setattr()	Sets an attribute (property/method) of an object
# * slice()	Returns a slice object
# * sorted()	Returns a sorted list
# * @staticmethod()	Converts a method into a static method
# * str()	Returns a string object
# * sum()	Sums the items of an iterator
# * super()	Returns an object that represents the parent class
# * tuple()	Returns a tuple
# * type()	Returns the type of an object
# * vars()	Returns the \_\_dict\_\_ property of an object
# * zip()	Returns an iterator, from two or more iterators}}}
# User Input# {{{
# https://www.w3schools.com/python/python_user_input.asp
# Python allows for user input.

# That means we are able to ask the user for input.

# The method is a bit different in Python 3.6 than Python 2.7.

# Python 3.6 uses the input() method.

# Python 2.7 uses the raw_input() method.

# The following example asks for the username, and when you entered the username, it gets printed on the screen:
username = input("Enter username:")
print("Username is: " + username)
Enter username:
# asdf
# Username is: asdf

username = raw_input("Enter username:")
print("Username is: " + username)
Enter username:
# asdf
# Username is: asdf

# Python stops executing when it comes to the input() function, and continues when the user has given some input.
# #}}}





# Type Conversion{{{


# You can convert from one type to another with the int(), float(), and complex() methods:
#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
# 1.0
# 2
# (1+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>
# Note: You cannot convert complex numbers into another number type.

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
# 6

# }}}


















# Python Scope{{{
# https://www.w3schools.com/python/python_scope.asp
# A variable is only available from inside the region it is created. This is called scope.
# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 300
  print(x)

myfunc()
# 300

# Function Inside Function
# As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
# 300

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
# 300
# 300


# even nested two or more levels deep
x = 300
def myfunc():
  print(x)
  def myinnerfunc():
    print(x)
    def innerinner():
        print(x)
    innerinner()
  myinnerfunc()
myfunc()
# 300
# 300
# 300

# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
# 200
# 300

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.
def myfunc():
  global x
  x = 300
myfunc()
print(x)
# 300

# Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
# 200

# if you dont use the global keyword inside the function, you can still change the values, but the changes dont persist outside the function
x = 300
def myfunc():
  
  x = 200
  print('inisde myfunc', x)
myfunc()
print(x)
# inisde myfunc 200
# 300



# In Python, the only construct that creates a new scope (other than the global scope) is a function. When a function is defined, a new local scope is created for that function. Variables defined within the function have local scope and are not accessible outside of the function, unless they are explicitly returned.
x = 0
if x == 0:
    y = 1
    print(y)
print(y)
# 1 
# y is accessible because if statement doesnt create new scope
# In this code, the if statement and the print statement are indented to the same level, but they do not create a new scope. The variable y is defined within the if statement, but it is still accessible outside of the if statement because it is defined in the global scope.

# #}}}






# Lambda functions{{{
# A lambda function is a small anonymous function.
a = 5
x = lambda : a + 10
print(x())
#15


# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))
# 15
# Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6))
# 30
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# 13

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
# 22

# Or, use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
# 33

# Or, use the same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
# 22
# 33
# Use lambda functions when an anonymous function is required for a short period of time.

# #}}}
# Recursion{{{
# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21#}}}
# Python Modules{{{
# https://www.w3schools.com/python/python_modules.asp
# What is a Module?
# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.
# navigate to mymodule.py in this directory to see the stuff we are importing for these examples
import mymodule
mymodule.greeting("Jonathan")
# Hello, Jonathan
# Note: When using a function from a module, use the syntax: module_name.function_name.

# Variables in Module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
import mymodule
a = mymodule.person1["age"]
print(a)
# 36

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
import mymodule as mx
a = mx.person1["age"]
print(a)
# 36

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import platform
x = platform.system()
print(x)
# Windows

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform
x = dir(platform)
print(x)
# ['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES', 'WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package __', '__spec__', '__version__', '_default_architecture', '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_perse_release_file', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'subprocess', 'sys', 'system', 'system_aliases', 'uname', 'uname_result', 'version', 'warnings', 'win32_ver']
# Note: The dir() function can be used on all modules, also the ones you create yourself.

# Import From Module
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1
print(person1["age"])
# 36
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

# #}}}

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
# 6












