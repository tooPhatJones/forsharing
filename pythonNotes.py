# python print function{{{
# The Python print() function is often used to output variables.
# https://www.w3schools.com/python/python_variables_output.asp
x = "Python is awesome"
print(x)
# Python is awesome
# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Python is awesome
# Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
# 15
x = 5
y = "John"
print(x + y)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)
# 5 John# 


# In Python 2.x, the print statement was used to output text to the console, and it did not require parentheses. For example:

# Copy
# Python 2.x
print "Hello, world!"
# In Python 3.x, the print function was introduced, and it requires parentheses around the string or other object that you want to print. For example:

# Python 3.x
print("Hello, world!")
# It is important to note that in Python 3.x, print is a function, not a statement, so it must be called with parentheses even if you are only printing a single object.

# In Python 2.x, you can use the print function by importing it from the __future__ module:

# Python 2.x with print function from __future__
from __future__ import print_function
print("Hello, world!")

# pypy
# it seems that pypy is smart enough to automatically interpret python 2 or 3 syntax somtimes. 
# both 
print('x')
# and 
print 'x' 
# work in pypy, where no paren breaks python3
# }}}

# primitive as well as non-primitive data structures# {{{
# Primitive Data Structures
# Integers
# Float
# Strings
# Boolean

# Non-Primitive Data Structures
# Arrays
# Lists
# Tuples
# Dictionary
# Sets
# Files# 

}}}
# Python Variables# {{{
# https://www.w3schools.com/python/python_variables.asp
x = 5
y = "John"
print(x)
print(y)
# 5
# John

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4
x = "Sally"
print(x)
# Sally

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)
# 3
# 3
# 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))
# <class 'int'>
# <class 'str'>

# String variables can be declared either by using single or double quotes:
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)
# John
# John

# Variable names are case-sensitive.
a = 4
A = "Sally"

print(a)
print(A)
# 4
# Sally


# }}}
# Variable Names# {{{
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
# John
# John
# John
# John
# John
# John

#This example will produce an error in the result
2myvar = "John"
my-var = "John"
my var = "John"
# Traceback (most recent call last):
  # File "/usr/lib/python3.7/py_compile.py", line 143, in compile
    # _optimize=optimize)
  # File "<frozen importlib._bootstrap_external>", line 791, in source_to_code
  # File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  # File "./prog.py", line 1
    # 2myvar = "John"
         # ^
# SyntaxError: invalid syntax

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
  # File "<string>", line 1, in <module>
  # File "/usr/lib/python3.7/py_compile.py", line 147, in compile
    # raise py_exc
# py_compile.PyCompileError:   File "./prog.py", line 1
    # 2myvar = "John"
         # ^
# SyntaxError: invalid syntax



# Remember that variable names are case-sensitive
# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:
# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# }}}
# assign Many Values to Multiple Variables# {{{
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Orange
# Banana
# Cherry


# Note: Make sure the number of variables matches the number of values, or else you will get an error.
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Orange
# Orange
# Orange

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# apple
# banana
# cherry# }}}
# Global Variables# {{{
# https://www.w3schools.com/python/python_variables_global.asp
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
# Python is awesome

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
# Python is fantastic
# Python is awesome


# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# Python is fantastic

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# Python is fantastic# }}}
# Data Types# {{{
# https://www.w3schools.com/python/python_datatypes.asp
# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
# You can get the data type of any object by using the type() function:
x = 5
print(type(x)) 
# <class 'int'>

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"#	str	
x = 20	# int	
x = 20.5# 	float	
x = 1j# 	complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})#	frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)#	bytearray	
x = memoryview(bytes(5))#	memoryview	
x = None	#NoneType

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it
x = str("Hello World")# 	str	
x = int(20)	# int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))#	tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)#	bytearray	
x = memoryview(bytes(5))	#memoryview# }}}
# none data type in python# {{{
# None is a data type in Python used to represent the absence of a value.

# Some key things about None:
# It's a singleton value, meaning only one None value exists.
# It's used to represent "no value" or "undefined" in Python.
# You can assign None to a variable to indicate that it has no value:
a = None

# None checks for equality using 'is' not '==':
# a is None # Checks if a is the same object as None  
# a == None # Checks if a has the same value as None 
# You can use None to default a function return value:
def get_data():
    # Get data not available 
    return None

# None evaluates to False in boolean context:
if a is None:
    print("a is None!") 
# None has a type of NoneType:
type(None) # Returns NoneType

None can be used to empty lists and clear variables:
a = [1,2,3]
a = None # Clear the list
b = "Hello"
b = None # Clear the string 

# So in summary, None represents the absence of a value in Python. It's used to:
# Indicate a variable has no meaningful value yet
# Default a function return value
# Empty containers like lists, dictionaries, etc.
# None evaluates to False in booleans and has a type of NoneType.
# }}}
# Python Numbers int float complex# {{{
# There are three numeric types in Python:

# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))
# <class 'int'>
# <class 'float'>
# <class 'complex'>

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
# <class 'int'>
# <class 'int'>
# <class 'int'>

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# <class 'float'>
# <class 'float'>
# <class 'float'>

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
# <class 'float'>
# <class 'float'>
# <class 'float'>

# Complex
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
# <class 'complex'>
# <class 'complex'>
# <class 'complex'>

# Type Conversion
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
# Python Casting# {{{
# https://www.w3schools.com/python/python_casting.asp
# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
# 1
# 2
# 3
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
# 1.0
# 2.8
# 3.0
# 4.2

# note non numerical characters in string will throw an error
r = float("4.2asdf")
print(r)
# Traceback (most recent call last):
  # File "./prog.py", line 4, in <module>
# ValueError: could not convert string to float: '4.2asdf'

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
# s1
# 2
# 3.0

# }}}

# python strings # {{{
# Ordered
# Immutable
# Homogeneous (only store character data)
# Accessed using index [] or slice []


# Python Strings# {{{
# https://www.w3schools.com/python/python_strings.asp
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
#You can use double or single quotes:
print("Hello")
print('Hello')
# Hello
# Hello

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)
# Hello


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
# Note: in the result, the line breaks are inserted at the same position as in the code.


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])
# e


# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x) 
# b
# a
# n
# a
# n
# a

# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))
# 13

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
# True

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Yes, 'free' is present.

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)
# True

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# No, 'expensive' is NOT present.# }}}
# Modify Strings# {{{
# https://www.w3schools.com/python/python_strings_modify.asp
a = "Hello, World!"
print(a.upper())
# HELLO, WORLD!

# Lower Case
a = "Hello, World!"
print(a.lower())
# hello, world!

# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
a = " Hello, World! "
print(a.strip())
# Hello, World!

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
# Jello, World!

# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
b = a.split(",")
print(b)
# ['Hello', ' World!']# }}}
# String Concatenation# {{{
# https://www.w3schools.com/python/python_strings_concatenate.asp
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
# HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# Hello World# }}}
# Format - Strings{{{
# https://www.w3schools.com/python/python_strings_format.asp
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt) 
# Traceback (most recent call last):
  # File "demo_string_format_error.py", line 2, in <module>
    # txt = "My name is John, I am " + age
# TypeError: must be str, not int

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# My name is John, and I am 36

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) 
# I want 3 pieces of item 567 for 49.95 dollars.

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 
# I want to pay 49.95 dollars for 3 pieces of item 567# }}}
# Escape Characters# {{{
# https://www.w3schools.com/python/python_strings_escape.asp
# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."


#You will get an error if you use double quotes inside a string that are surrounded by double quotes:
 File "demo_string_escape_error.py", line 1
    txt = "We are the so-called "Vikings" from the north."
                                       ^
# SyntaxError: invalid syntax
# To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
# We are the so-called "Vikings" from the north.



# Escape Characters
# Other escape characters used in Python:

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# }}}
# String Methods# {{{
# https://www.w3schools.com/python/python_strings_methods.asp
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning# }}}

# }}}
# python lists {{{
# lists are 
# Ordered
# Allow duplicate elements
# Allow heterogeneous elements (different types)
# Changable (elements can be added or removed)
# Accessed using index []

# Python Lists# {{{
# https://www.w3schools.com/python/python_lists.asp
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)
# ['apple', 'banana', 'cherry']

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
['apple', 'banana', 'cherry', 'apple', 'cherry']

# List Length
# To determine how many items a list has, use the len() function:
# thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# 3

# List Items - Data Types
# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# ['abc', 34, True, 40, 'male']

type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# <class 'list'>

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# ['apple', 'banana', 'cherry']

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# }}}
# Access List Items# {{{
# https://www.w3schools.com/python/python_lists_access.asp
# List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# banana
# Note: The first item has index 0.

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# cherry

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
['cherry', 'orange', 'kiwi']
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# Remember that the first item has index 0.
# By leaving out the start value, the range will start at the first item:
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
['apple', 'banana', 'cherry', 'orange']


# By leaving out the end value, the range will go on to the end of the list:
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
['orange', 'kiwi', 'melon']

# Check if Item Exists in keyword
# To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Yes, 'apple' is in the fruits list
# }}}
# Change List Items# {{{
# https://www.w3schools.com/python/python_lists_change.asp
# Change Item Value
# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# ['apple', 'blackcurrant', 'cherry']

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'cherry']
# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# ['apple', 'watermelon']

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
# ['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
# ['apple', 'banana', 'watermelon', 'cherry']
# Note: As a result of the example above, the list will now contain 4 items.# }}}
# Add List Items# {{{
# https://www.w3schools.com/python/python_lists_add.asp

# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange']

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# ['apple', 'orange', 'banana', 'cherry']
# Note: As a result of the examples above, the lists will now contain 4 items.

# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
# The elements will be added to the end of the list.

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']# }}}
# Remove List Items# {{{
# https://www.w3schools.com/python/python_lists_remove.asp
# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry']

# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ['banana', 'cherry']

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
# Traceback (most recent call last):
  # File "demo_list_del2.py", line 3, in <module>
    # print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
# NameError: name 'thislist' is not defined

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []# }}}
# Loop Lists# {{{
# https://www.w3schools.com/python/python_lists_loop.asp
# Loop Through a List
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# apple
# banana
# cherry

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
 # apple
 # banana
 # cherry
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# apple
 # banana
 # cherry
# The iterable created in the example above is [0, 1, 2].

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
 # apple
 # banana
 # cherry

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
 # apple
 # banana
 # cherry# }}}
# List Comprehension# {{{
# https://www.w3schools.com/python/python_lists_comprehension.asp
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
# ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# ['apple', 'banana', 'mango']
# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# ['banana', 'cherry', 'kiwi', 'mango']
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# The condition is optional and can be omitted:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
['apple', 'banana', 'cherry', 'kiwi', 'mango']
# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]
print(newlist)
# [0, 1, 2, 3, 4]
# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
# You can set the outcome to whatever you like:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
# ['hello', 'hello', 'hello', 'hello', 'hello']
# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']
# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".
# }}}
# Sort Lists# {{{
# https://www.w3schools.com/python/python_lists_sort.asp

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# [23, 50, 65, 82, 100]

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# [100, 82, 65, 50, 23]

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# [50, 65, 23, 82, 100]

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 
# ['cherry', 'Kiwi', 'Orange', 'banana']# }}}
 # Copy Lists# {{{
# https://www.w3schools.com/python/python_lists_copy.asp
# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# ['apple', 'banana', 'cherry']
# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# ['apple', 'banana', 'cherry']# }}}
# Join Lists# {{{
# https://www.w3schools.com/python/python_lists_join.asp

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# ['a', 'b', 'c', 1, 2, 3]
# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
# ['a', 'b', 'c', 1, 2, 3]
# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# ['a', 'b', 'c', 1, 2, 3]# }}}
# List Methods# {{{
# https://www.w3schools.com/python/python_lists_methods.asp
# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list# }}}
# }}}
# Python Tuples<!----># {{{
# Ordered
# Immutable (elements cannot be added or removed)
# Allow duplicate elements
# Allow heterogeneous elements
# Accessed using index []

# tuples {{{
# https://www.w3schools.com/python/python_tuples.asp
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
('apple', 'banana', 'cherry')

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuple Length
# To determine how many items a tuple has, use the len() function:
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
# 3

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# <class 'tuple'>
# <class 'str'>
# Tuple Items - Data Types
# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
# ('apple', 'banana', 'cherry')
# (1, 5, 7, 9, 3)
# (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
('abc', 34, True, 40, 'male')
type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'># }}}
# Access Tuple Items# {{{
# https://www.w3schools.com/python/python_tuples_access.asp
# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# banana
# Note: The first item has index 0.

# Negative Indexing
# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# cherry

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
('cherry', 'orange', 'kiwi')
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.
# By leaving out the start value, the range will start at the first item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# ('apple', 'banana', 'cherry', 'orange')

# By leaving out the end value, the range will go on to the end of the list:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# ('cherry', 'orange', 'kiwi', 'melon', 'mango')
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#Negative indexing means starting from the end of the tuple.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,
# ('orange', 'kiwi', 'melon')

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# Yes, 'apple' is in the fruits tuple# }}}
# Update Tuples# {{{
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# ("apple", "kiwi", "cherry")
# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')
# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# ('apple', 'banana', 'cherry', 'orange')
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
# Remove Items
# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# ('banana', 'cherry')

# Or you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
# Traceback (most recent call last):
  # File "demo_tuple_del.py", line 3, in <module>
    # print(thistuple) #this will raise an error because the tuple no longer exists
# NameError: name 'thistuple' is not defined
# }}}
# Unpack Tuples<!----># {{{
# https://www.w3schools.com/python/python_tuples_unpack.asp
# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)
# ('apple', 'banana', 'cherry')
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
# apple
# banana
# cherry

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']
# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
# apple
# ['mango', 'papaya', 'pineapple']
# cherry<!----># }}}
# Loop Tuples{{{
# https://www.w3schools.com/python/python_tuples_loop.asp
# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# apple
# banana
# cherry
# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# apple
# banana
# cherry
# Using a While Loop
# You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# apple
# banana
# cherry

# Join Tuples
# https://www.w3schools.com/python/python_tuples_join.asp
# Join Two Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# ('a', 'b', 'c', 1, 2, 3)
# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')}}}
# Tuple Methods# {{{
# https://www.w3schools.com/python/python_tuples_methods.asp
# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found# }}}
# }}}
# python sets{{{
# Unordered
# Don't allow duplicate elements
# Allow heterogeneous elements
# Changable
# Accessed using in and not in operators


# Python Sets# {{{
# https://www.w3schools.com/python/python_sets.asp
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
# {'banana', 'cherry', 'apple'}

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# {'banana', 'cherry', 'apple'}
# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# {True, 2, 'banana', 'cherry', 'apple'}
# Get the Length of a Set
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# 3
# Set Items - Data Types
# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
# {'cherry', 'apple', 'banana'}
# {1, 3, 5, 7, 9}
# {False, True}
# A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# {True, 34, 40, 'male', 'abc'}

# Type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
# {'apple', 'cherry', 'banana'}

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove items and add new items.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.# }}}
# Access Set Items# {{{
# https://www.w3schools.com/python/python_sets_access.asp
# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# cherry
# apple
# banana

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# True
# Change Items
# Once a set is created, you cannot change its items, but you can add new items.# }}}
# Add Set Items# {{{
# https://www.w3schools.com/python/python_sets_add.asp
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# {'banana', 'apple', 'cherry', 'orange'}

# Add Sets
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# {'banana', 'cherry', 'apple', 'orange', 'kiwi'}# }}}
# Remove Set Items# {{{
# https://www.w3schools.com/python/python_sets_remove.asp
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# {'apple', 'cherry'}
# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# {'apple', 'cherry'}
# Note: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
# apple
# {'cherry', 'banana'}
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# set()
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this will raise an error because the set no longer exists
# Traceback (most recent call last):
  # File "demo_set_del.py", line 5, in <module>
    # print(thisset) #this will raise an error because the set no longer exists
# NameError: name 'thisset' is not defined# }}}
# Loop Sets# {{{
# https://www.w3schools.com/python/python_sets_loop.asp
# Loop Items
# You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# banana
# apple
# cherry# }}}
# Set Methods# {{{
# https://www.w3schools.com/python/python_sets_methods.asp
# Python has a set of built-in methods that you can use on sets.

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others# }}}
# }}}
# dictionaries {{{
# Unordered
# Store data as key-value pairs
# Require unique keys (no duplicate keys)
# Allow heterogeneous values
# Changable
# Accessed using keys [] or .get()



# Python Dictionaries# {{{
# https://www.w3schools.com/python/python_dictionaries.asp
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Ford

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
# 3

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
# <class 'dict'>
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
# <class 'dict'>

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
# {'name': 'John', 'age': 36, 'country': 'Norway'}
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.# }}}
# Access Dictionary Items# {{{
# https://www.w3schools.com/python/python_dictionaries_access.asp
# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
# Mustang

# There is also a method called get() that will give you the same result:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
# Mustang

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
# dict_keys(['brand', 'model', 'year'])
The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
# dict_keys(['brand', 'model', 'year'])
# dict_keys(['brand', 'model', 'year', 'color'])
# Get Values
# The values() method will return a list of all the values in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)
# dict_values(['Ford', 'Mustang', 1964])
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)
# dict_values(['Ford', 'Mustang', 1964])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 2020])
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
# car["color"] = "red"
print(x) #after the change
# dict_values(['Ford', 'Mustang', 1964])
# dict_values(['Ford', 'Mustang', 1964, 'red'])

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Yes, 'model' is one of the keys in the thisdict dictionary# }}}
# Change Dictionary Items# {{{
# https://www.w3schools.com/python/python_dictionaries_change.asp
# Change Values
# You can change the value of a specific item by referring to its key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}# }}}
# Add Dictionary Items# {{{
# https://www.w3schools.com/python/python_dictionaries_add.asp
# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}# }}}
# Remove Dictionary Items# {{{
# https://www.w3schools.com/python/python_dictionaries_remove.asp
# Removing Items
# There are several methods to remove items from a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# {'brand': 'Ford', 'year': 1964}
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang'}
# The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# {'brand': 'Ford', 'year': 1964}
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.
# Traceback (most recent call last):
  # File "demo_dictionary_del3.py", line 7, in <module>
    # print(thisdict) #this will cause an error because "thisdict" no longer exists.
# NameError: name 'thisdict' is not defined
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# {}

# }}}
# Loop Dictionaries# {{{
# https://www.w3schools.com/python/python_dictionaries_loop.asp
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# brand
# model
# year
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
# Ford
# Mustang
# 1964
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
# Ford
# Mustang
# 1964
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
# brand
# model
# year
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
# brand Ford
# model Mustang
# year 1964# }}}
# Copy Dictionaries# {{{
# https://www.w3schools.com/python/python_dictionaries_copy.asp
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}# }}}
# Nested Dictionaries# {{{
# https://www.w3schools.com/python/python_dictionaries_nested.asp
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
# {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
# Or, if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
# {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
# Tobias# }}}
# Dictionary Methods# {{{
# https://www.w3schools.com/python/python_dictionaries_methods.asp
# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
# # }}}
# }}}

# Python Booleans# {{{
# https://www.w3schools.com/python/python_booleans.asp
# Booleans represent one of two values: True or False.
# Boolean Values
# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)
# True
# False
# False

# When you run a condition in an if statement, Python returns True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
a = 200
b = 33
# b is not greater than a

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))
True
True
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
# True
# True

# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# True
# True
# True

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# False
# False
# False
# False
# False
# False
# False

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# False

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:
def myFunction() :
  return True
print(myFunction())
# True

# You can execute code based on the Boolean answer of a function:
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
# YES!

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
# True

# }}}
# Python Operators# {{{
# https://www.w3schools.com/python/python_operators.asp
# Python Operators
# Operators are used to perform operations on variables and values.

# In the example below, we use the + operator to add together two values:
print(10 + 5)
# 15


# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:
# Operator	Name	Example
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division (includes remainder as float)	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division (rounds down to nearest int)	x // y


# Python Assignment Operators
# Assignment operators are used to assign values to variables:
# Operator	Example	       Same As	
# =	x = 5	x = 5	
# +=	    x += 3	       x = x + 3	
# -=	    x -= 3	       x = x - 3	
# *=	    x *= 3	       x = x * 3	
# /=	    x /= 3	       x = x / 3	
# %=	    x %= 3	       x = x % 3	
# //=	    x //= 3	       x = x // 3	
# **=	    x **= 3	       x = x ** 3	
# &=	    x &= 3	       x = x & 3	
# |=	    x |= 3	       x = x | 3	
# ^=	    x ^= 3	       x = x ^ 3	
# >>=	    x >>= 3	       x = x >> 3	
# <<=	    x <<= 3	       x = x << 3
# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

# Python Logical Operators (combine boolean expressions)
# Logical operators are used to combine conditional statements:

# Operator	Description	Example
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# note using the ! operator instead of the not operator will throw an error
print(not(5<4 or 3<4))# prints false
print(!(5<4 or 3<4)) # throws error

# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	Description	Example
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y
# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description	Example

# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# Operator Precedence
# Operator precedence describes the order in which operations are performed.
print((6 + 3) - (6 + 3))
# Parenthesis have the highest precedence, and need to be evaluated first.
# The calculation above reads 9 - 9 = 0
# 0

print(100 + 5 * 3)
# Multiplication has higher precedence than addition, and needs to be evaluated first.
# The calculation above reads 100 + 15 = 115
# 115

# The precedence order is described in the table below, starting with the highest precedence at the top:
# Operator	Description
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR	


# If two operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3)
# Additions and subtractions have the same precedence, and we need to calculate from left to right.
# The calculation above reads:
# 5 + 4 = 9
# 9 - 7 = 2
# 2 + 3 = 5

# 5# }}}

# Python Functions{{{
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
# }}}
# arbitrary args{{{
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#The youngest child is Linus

def my_function(*kids):
  print("The youngest child is " + kids[4])
my_function("Emil", "Tobias", "Linus")
# Traceback (most recent call last):
  # File "/home/mrtophatjones/n/python/forExecution.py", line 3, in <module>
    # my_function("Emil", "Tobias", "Linus")
  # File "/home/mrtophatjones/n/python/forExecution.py", line 2, in my_function
    # print("The youngest child is " + kids[4])
# IndexError: tuple index out of range

def my_function(*fname, lname):
  print(fname + " " + lname)
my_function("Emil") #error
# Traceback (most recent call last):
  # File "/home/mrtophatjones/n/python/forExecution.py", line 3, in <module>
    # my_function("Emil") #error
# TypeError: my_function() missing 1 required keyword-only argument: 'lname'

# cant have more than 1 arbitrary args
def my_function(*fname, *lname):
  print(fname + " " + lname)
my_function("Emil") #error
# File "/home/mrtophatjones/n/python/forExecution.py", line 1
    # def my_function(*fname, *lname):
                            # ^
# SyntaxError: invalid syntax

#print number of args
def manyArgs(*arg):
  print ("I was called with", len(arg), "arguments:", arg)
manyArgs(1,2,3,4) #I was called with 4 arguments: (1, 2, 3, 4)




# Sometimes you don't want to specify the number of arguments and want to use keys for them (the compiler will complain if one argument passed in a dictionary is not used in the method).

def manyArgs1(args):
  print args.a, args.b #note args.c is not used here

def manyArgs2(args):
  print args.c #note args.b and .c are not used here

class Args: pass

args = Args()
args.a = 1
args.b = 2
args.c = 3
manyArgs1(args) #outputs 1 2
manyArgs2(args) #outputs 3

# Then you can do things like
myfuns = [manyArgs1, manyArgs2]
for fun in myfuns:
  fun(args)
# 1 2
# 3

# }}}
# key value arguments{{{
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#The youngest child is Linus
# }}}
# Arbitrary Keyword Arguments, **kwargs{{{
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# His last name is Refsnes


# And you can mix the two:
def myfunc2(*args, **kwargs):
   for a in args:
       print a
   for k,v in kwargs.iteritems():
       print "%s = %s" % (k, v)
myfunc2(1, 2, 3, banan=123)
# 1
# 2
# 3
# banan = 123
# They must be both declared and called in that order, that is the function signature needs to be *args, **kwargs, and called in that order.


# }}}
# Default Parameter Value{{{
# The following example shows how to use a default parameter value.
def my_function(country = "Norway"):
  print("I am from " + country)
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

# }}}
# Passing a List as an Argument{{{
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
# apple
# banana
# cherry
# }}}
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



# }}}
# The pass Statement# {{{
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass
  # having an empty function definition like this, would raise an error without the pass statement}}}
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
# 21}}}
# }}}
# If ... Else{{{
# https://www.w3schools.com/python/python_conditions.asp
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.
a = 33
b = 200
if b > a:
  print("b is greater than a")
# b is greater than a

# If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
  # File "demo_if_error.py", line 4
    # print("b is greater than a")
        # ^
# IndentationError: expected an indented block

# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# a and b are equal

# Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# a is greater than b

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# b is not greater than a

# Short Hand If
if a > b: print("a is greater than b")
# "a is greater than b"

# Short Hand If ... Else or ternary operator. if true do first thing, if not, do second thing
a = 2
b = 330
print("A") if a > b else print("B")
# B

# You can also have multiple else statements (ternary operators) on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# =

# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# Both conditions are True

# Or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# At least one of the conditions is True

# Not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# a is NOT greater than b

# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
# Above ten,
# and also above 20!

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement



# }}}
# there is no switch in python if you want to create somthing like a switch just use if, elif, else:

#infinie loops in python# {{{
count = 0
while True:
    count += 1
    print(count)
# this loop will increment forever and cause python to hang, and the processor core its running on to stall. 
# What happens when you run an infinite loop in Python is:

# The loop code will continue executing indefinitely.
# The program will become unresponsive and "hung".
# The CPU usage will go to 100% as the loop runs continuously.
# You will not be able to interrupt the program normally.
# The only way to stop an infinite loop in Python is to:

# Kill the Python process (in the OS task manager)
# Hit Ctrl + C in the terminal to send a SIGINT signal and interrupt the program.

# An infinite loop in Python itself will not directly crash your computer. However, it can indirectly cause issues if left running for a long time.

# When you have an infinite loop running in a Python program, it will:
# Use up CPU resources - The CPU usage will go to 100% since the loop is running continuously. This can slow down other processes on your computer.
# Use up memory - If the loop is allocating new objects in memory on each iteration, it can eventually consume all available memory.
# Make the Python process unresponsive - You will not be able to interrupt the program normally since it's stuck in the infinite loop.

# However, your computer is unlikely to completely "crash" due to an infinite loop in Python. More likely, you'll experience:
# Slow performance - Other programs will run slowly due to high CPU usage.
# Program freezing - The Python program itself will become unresponsive and "hang".

# But your operating system is designed to handle situations like this, and it has mechanisms to interrupt and kill runaway processes. 

# Only in extreme cases, where the infinite loop is consuming a massive amount of resources for an extended period, it could potentially cause issues like:

# Kernel panic (for Linux) - If memory usage goes too high.
# Blue screen of death (for Windows) - Again, due to excessive memory consumption.
# }}}

# Why are there no ++ and -- operators in Python?# {{{
# https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python#:~:text=Because%2C%20in%20Python%2C%20integers%20are,actually%20returns%20a%20different%20object).
# python doesnt include these operators because they are essentially extra
 # }}}
# For Loops{{{
# https://www.w3schools.com/python/python_for_loops.asp
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
  # print(x)
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
# having an empty for loop like this, would raise an error without the pass statement}}}
# While Loops{{{
i = 1
while i < 6:
  print(i)
  i += 1
# 1
# 2
# 3
# 4
# 5

# Note: remember to increment I, or else the loop will continue forever.

# The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# 1
# 2
# 3

# The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# 1
# 2
# 4
# 5
# 6

# The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6}}}
# Lambda functions{{{
# A lambda function is a small anonymous function.
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

# }}}
# Arrays{{{
# https://www.w3schools.com/python/python_arrays.asp
# Python does not have built-in support for Arrays, but Python Lists can be used instead.
# This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# ['Ford', 'Volvo', 'BMW']
# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?

# The solution is an array!

# An array can hold many values under a single name, and you can access the values by referring to an index number.
# Access the Elements of an Array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Ford
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
# ['Toyota', 'Volvo', 'BMW']

The Length of an Array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
# 3
# Note: The length of an array is always one more than the highest array index.

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
# Ford
# Volvo
# BMW

# Adding Array Elements
# You can use the append() method to add an element to an array.
cars.append("Honda")
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
# ['Ford', 'Volvo', 'BMW', 'Honda']

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
# ['Ford', 'BMW']
# You can also use the remove() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
# ['Ford', 'BMW']
# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# }}}
# Python Classes and Objects{{{
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.
# Create a Class
class MyClass:
  x = 5
print(MyClass)
# <class '__main__.MyClass'>

# Create Object
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
5

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name) # John
print(p1.age) # 36
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)
# <__main__.Person object at 0x15039e602100>


# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"    
p1 = Person("John", 36)
print(p1) # John(36)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
# Hello my name is John
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
Hello my name is John
Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1.age = 40
print(p1.age)
# 40

# Delete Object Properties
# You can delete properties on objects by using the del keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)
# Traceback (most recent call last):
  # File "demo_class7.py", line 13, in <module>
    # print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'

# Delete Objects
# You can delete objects by using the del keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)
# Traceback (most recent call last):
  # File "demo_class8.py", line 13, in <module>
    # print(p1)
# NameError: 'p1' is not defined

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement}}}
# Python Inheritance{{{
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.
# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
# John Doe

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# Now the Student class has the same properties and methods as the Person class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
# Mike Olsen

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
# Mike Olsen

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
# Mike Olsen
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
# 2019
# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
# 2019

# Add Methods
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome()
# Welcome Mike Olsen to the class of 2019
# }}}
#python abstract classes# {{{
# Yes, Python has abstract classes, which are defined using the abc module. An abstract class is a class that cannot be instantiated, but can be subclassed. It is used to define a common interface for a group of related classes.

# To define an abstract class in Python, you can use the ABC class provided by the abc module as a base class for your abstract class. You can then use the @abstractmethod decorator to mark certain methods as abstract methods that must be implemented by any subclass.

# Here's an example:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# In this example, the Shape class is an abstract class with two abstract methods area() and perimeter(). Any subclass of Shape must implement these methods.

# Note that attempting to instantiate an abstract class will result in a TypeError. For example, the following code will raise a TypeError:
s = Shape() # Raises TypeError
Instead, you can instantiate a subclass of Shape that implements the abstract methods:

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius
c = Circle(5)
print(c.area()) # Output: 78.5
print(c.perimeter()) # Output: 31.4




# }}}
# Python Iterators{{{
# https://www.w3schools.com/python/python_iterators.asp
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
# apple
# banana
# cherry
Even strings are iterable objects, and can return an iterator:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# b
# a
# n
# a
# n
# a
# We can also use a for loop to iterate through an iterable object:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
# apple
# banana
# cherry
mystr = "banana"
for x in mystr:
  print(x)
# b
# a
# n
# a
# n
# a
# The for loop actually creates an iterator object and executes the next() method for each loop.

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# 1
# 2
# 3
# 4
# 5

# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20


# }}}
# Polymorphism{{{
# https://www.w3schools.com/python/python_polymorphism.asp
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# An example of a Python function that can be used on different objects is the len() function.
x = "Hello World!"
print(len(x))
# 12

# Tuple
# For tuples len() returns the number of items in the tuple:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
# 3

# Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
# 3
# }}}
# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class
for x in (car1, boat1, plane1):
  x.move()
# Drive!
# Sail!
# Fly!
# Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.
# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
# Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!
# Child classes inherits the properties and methods from the parent class.
# In the example above you can see that the Car class i empty, but it inherits brand, model, and move() from Vehicle.
# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.
# Because of polymorphism we can execute the same method for all classes.


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
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
    def innerinner():
        print(x)
    innerinner()
  myinnerfunc()
myfunc()
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

# }}}
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

# }}}

# Python Datetime# {{{
# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
x = datetime.datetime.now()
print(x)
# 2023-05-22 17:39:47.993052

# Date Output
# When we execute the code from the example above the result will be:
# 2023-05-22 17:39:23.378724
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.
# Here are a few examples, you will learn more about them later in this chapter:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
# 2023
# Monday

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
# 2023
# Monday

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
# 2020-05-17 00:00:00
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
# June

# A reference of all the legal format codes:

# Directive	Description	Example	Try it
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01	
# # }}}

# Math# {{{
# https://www.w3schools.com/python/python_math.asp
# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
# 5
# 25

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)
# 7.25

# The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3)
print(x)
# 64

# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:
# import math
# When you have imported the math module, you can start using methods and constants of the module.
# The math.sqrt() method for example, returns the square root of a number:
import math
x = math.sqrt(64)
print(x)
# 8.0

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
#Import math library
import math
#Round a number upward to its nearest integer
x = math.ceil(1.4)
#Round a number downward to its nearest integer
y = math.floor(1.4)
print(x)
print(y)
# 2
# 1

# The math.pi constant, returns the value of PI (3.14...):
import math
x = math.pi
print(x)
# 3.141592653589793

# Python JSON
# https://www.w3schools.com/python/python_json.asp
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.
import json
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
# 30

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
# {"name": "John", "age": 30, "city": "New York"}

# You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
# {"name": "John", "age": 30}
# ["apple", "bananas"]
# ["apple", "bananas"]
# "hello"
# 42
# 31.76
# true
# false
# null

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# {
    # "name": "John",
    # "age": 30,
    # "married": true,
    # "divorced": false,
    # "children": [
        # "Ann",
        # "Billy"
    # ],
    # "pets": null,
    # "cars": [
        # {
            # "model": "BMW 230",
            # "mpg": 27.5
        # },
        # {
            # "model": "Ford Edge",
            # "mpg": 24.1
        # }
    # ]
# }
# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# {
    # "name" = "John".
    # "age" = 30.
    # "married" = true.
    # "divorced" = false.
    # "children" = [
        # "Ann".
        # "Billy"
    # ].
    # "pets" = null.
    # "cars" = [
        # {
            # "model" = "BMW 230".
            # "mpg" = 27.5
        # }.
        # {
            # "model" = "Ford Edge".
            # "mpg" = 24.1
        # }
    # ]
# }

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
# {
    # "age": 30,
    # "cars": [
        # {
            # "model": "BMW 230",
            # "mpg": 27.5
        # },
        # {
            # "model": "Ford Edge",
            # "mpg": 24.1
        # }
    # ],
    # "children": [
        # "Ann",
        # "Billy"
    # ],
    # "divorced": false,
    # "married": true,
    # "name": "John",
    # "pets": null
# }


# }}}
# Python RegEx# {{{
# https://www.w3schools.com/python/python_regex.asp
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.
# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:
# When you have imported the re module, you can start using regular expressions:
import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
# YES! We have a match!

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

# Metacharacters
# Metacharacters are characters with a special meaning:
# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group
# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

# The findall() Function
# The findall() function returns a list containing all matches.

import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# ['ai', 'ai']
# The list contains the matches in the order they are found.
# If no matches are found, an empty list is returned:

import re
txt = "The rain in Spain"
#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)
# []
# No match

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
# []
# No match

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
# The first white-space character is located in position: 3
# If no matches are found, the value None is returned:

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
# None

# The split() Function
# The split() function returns a list where the string has been split at each match:
import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# ['The', 'rain', 'in', 'Spain']
# You can control the number of occurrences by specifying the maxsplit parameter:

import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# ['The', 'rain in Spain']

# The sub() Function
# The sub() function replaces the matches with the text of your choice:
import re
#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
The9rain9in9Spain
You can control the number of replacements by specifying the count parameter:
import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# The9rain9in Spain

# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
import re
#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
# <_sre.SRE_Match object; span=(5, 7), match='ai'>
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
import re
#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# (12, 17)

import re
#The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# The rain in Spain
import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# Spain
# Note: If there is no match, the value None will be returned, instead of the Match Object.
# }}}

# Python Try Except# {{{
# https://www.w3schools.com/python/python_try_except.asp
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:
# #The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
# An exception occurred
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:
#This will raise an exception, because x is not defined:
print(x)
# Traceback (most recent call last):
  # File "demo_try_except_error.py", line 3, in <module>
    # print(x)
# NameError: name 'x' is not defined

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

#The try block will generate a NameError, because x is not defined:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# Variable x is not defined

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
#The try block does not raise any errors, so the else block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# Hello
# Nothing went wrong

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# Something went wrong
# The 'try except' is finished
# This can be useful to close objects and clean up resources:
#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
# Something went wrong when writing to the file
# The program can continue, without leaving the file object open.


# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
# Traceback (most recent call last):
  # File "demo_ref_keyword_raise.py", line 4, in <module>
    # raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero

# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user.
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
# Traceback (most recent call last):
  # File "demo_ref_keyword_raise2.py", line 4, in <module>
    # raise TypeError("Only integers are allowed")
# TypeError: Only integers are allowed

# }}}
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
# }}}

# String Formatting# {{{
# https://www.w3schools.com/python/python_string_formatting.asp
# To make sure a string will display as expected, we can format the result with the format() method.

# String format()
# The format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# The price is 49 dollars
# You can add parameters inside the curly brackets to specify how to convert the value:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
# The price is 49.00 dollars

# Multiple Values
# If you want to use more values, just add more values to the format() method:
print(txt.format(price, itemno, count))
# And add more placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item number 567 for 49.00 dollars.

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item number 567 for 49.00 dollars.

# Also, if you want to refer to the same value more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
# His name is John. John is 36 years old.

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
# I have a Ford, it is a Mustang.



# }}}
# “Old Style” String Formatting (% Operator)# {{{

# https://realpython.com/python-string-formatting/
# Strings in Python have a unique built-in operation that can be accessed with the % operator. This lets you do simple positional formatting very easily. If you’ve ever worked with a printf-style function in C, you’ll recognize how this works instantly. Here’s a simple example:
'Hello, %s' % name
"Hello, Bob"
# Here, you can use the %x format specifier to convert an int value to a string and to represent it as a hexadecimal number:
'%x' % errno
# 'badc0ffee'

# The “old style” string formatting syntax changes slightly if you want to make multiple substitutions in a single string. Because the % operator takes only one argument, you need to wrap the right-hand side in a tuple, like so:
'Hey %s, there is a 0x%x error!' % (name, errno)
# 'Hey Bob, there is a 0xbadc0ffee error!'

# It’s also possible to refer to variable substitutions by name in your format string, if you pass a mapping to the % operator:
'Hey %(name)s, there is a 0x%(errno)x error!' % {
...     "name": name, "errno": errno }
# 'Hey Bob, there is a 0xbadc0ffee error!'
# }}}
# String Interpolation / f-Strings (Python 3.6+)# {{{

# https://realpython.com/python-string-formatting/
# Python 3.6 added a new string formatting approach called formatted string literals or “f-strings”. This new way of formatting strings lets you use embedded Python expressions inside string constants. Here’s a simple example to give you a feel for the feature:
f'Hello, {name}!'
# 'Hello, Bob!'

# As you can see, this prefixes the string constant with the letter “f“—hence the name “f-strings.” This new formatting syntax is powerful. Because you can embed arbitrary Python expressions, you can even do inline arithmetic with it. Check out this example:
a = 5
b = 10
f'Five plus ten is {a + b} and not {2 * (a + b)}.'
# 'Five plus ten is 15 and not 30.'

# Formatted string literals are a Python parser feature that converts f-strings into a series of string constants and expressions. They then get joined up to build the final string.

# Imagine you had the following greet() function that contains an f-string:
def greet(name, question):
...     return f"Hello, {name}! How's it {question}?"
...
greet('Bob', 'going')
# "Hello, Bob! How's it going?"

# When you disassemble the function and inspect what’s going on behind the scenes, you’ll see that the f-string in the function gets transformed into something similar to the following:
def greet(name, question):
    return "Hello, " + name + "! How's it " + question + "?"
# The real implementation is slightly faster than that because it uses the BUILD_STRING opcode as an optimization. But functionally they’re the same:
import dis
dis.dis(greet)
 # 2           0 LOAD_CONST               1 ('Hello, ')
              # 2 LOAD_FAST                0 (name)
              # 4 FORMAT_VALUE             0
              # 6 LOAD_CONST               2 ("! How's it ")
              # 8 LOAD_FAST                1 (question)
             # 10 FORMAT_VALUE             0
             # 12 LOAD_CONST               3 ('?')
             # 14 BUILD_STRING             5
             # 16 RETURN_VALUE

# String literals also support the existing format string syntax of the str.format() method. That allows you to solve the same formatting problems we’ve discussed in the previous two sections:
f"Hey {name}, there's a {errno:#x} error!"
"Hey Bob, there's a 0xbadc0ffee error!"
# Python’s new formatted string literals are similar to JavaScript’s Template Literals added in ES2015. I think they’re quite a nice addition to Python, and I’ve already started using them in my day to day (Python 3) work. You can learn more about formatted string literals in our in-depth Python f-strings tutorial.# }}}
# template strings# {{{
# Template strings in Python are string literals that allow variable substitution. They use the .format() method to interpolate variables into the string.
# Template strings are declared using double curly brackets:

name = "John"
age = 30
s = f"Hello, my name is {{name}} and I'm {{age}} years old."
# String before formatting:
print(s)  
# Hello, my name is {{name}} and I'm {{age}} years old.
# String after formatting:
print(s.format(name=name, age=age))   
# Hello, my name is John and I'm 30 years old.

# Here we declare a string s with curly bracket placeholders {{name}} and {{age}}.

# We then call .format() and pass the variable values as keyword arguments. This substitutes the variable values into the placeholders in the string.

# We can have multiple placeholders:
color = "blue"
food = "pizza"
s = "I love to eat {{food}} and my favorite color is {{color}}."
print(s.format(food=food, color=color))
# I love to eat pizza and my favorite color is blue.   
# The .format() method also supports positional arguments:

name = "John"
age = 30
s = "Hello, my name is {!s} and I'm {!d} years old."
print(s.format(name, age))  
# Hello, my name is John and I'm 30 years old.
# Here we use {!s} and {!d} to specify that the first argument is a string and second is an int.# }}}
# Python File handling# {{{
# https://www.w3schools.com/python/python_file_handling.asp
# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)
# To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
# The code above is the same as:

f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# Note: Make sure the file exists, or else you will get an error.

# Open a File in the same directory as this file, demofile.txt
# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# If the file is located in a different location, "D:\\myfiles\welcome.txt" you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("demofile.txt", "r")
print(f.read(5))
# Hello! Welcome to demofile.txt

# Read Lines
# You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())
# Hello! Welcome to demofile.txt

# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.

# By looping through the lines of the file, you can read the whole file, line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# Close Files
# It is a good practice to always close the file when you are done with it.
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Hello! Welcome to demofile.txt
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.


# Python File Write
# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
# Hello! Welcome to demofile2.txt
# This file is for testing purposes.
# Good Luck!Now the file has more content!
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
# Woops! I have deleted the content!
# Note: the "w" method will overwrite the entire file.

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist
f = open("myfile.txt", "x")
# Result: a new empty file is created!
# Create a new file if it does not exist:
f = open("myfile.txt", "w")


# Python Delete File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demofile.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
import os
os.rmdir("myfolder")
# Note: You can only remove empty folders.




# }}}


