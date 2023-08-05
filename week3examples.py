
# python lists {{{
# lists are 
# Ordered
# Allow duplicate elements
# Allow heterogeneous elements (different types)
# Changable (elements can be added or removed)
# Accessed using index []

#slicing notation# {{{
# In Python, list slicing notation is a way to extract a portion of a list based on its indices. The general syntax for list slicing is:
# list[start:stop:step]
# where:

# list is the list you want to slice
# start is the index of the first element you want to include in the slice (default is 0)
# stop is the index of the first element you want to exclude from the slice (default is the length of the list)
# step is the size of the step between elements in the slice (default is 1)
# Here are some examples of how to use list slicing notation:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_three = my_list[0:3]  # [1, 2, 3]
last_three = my_list[-3:]  # [8, 9, 10]
every_other = my_list[::2]  # [1, 3, 5, 7, 9]
# Reverse the list
reversed_list = my_list[::-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# you can use a start index that is greater than the end index when slicing a list with a negative step. In this case, the resulting list will contain elements in reverse order, starting from the start index and ending at the end index. Here's an example:

# Get elements of the list in reverse order, starting from index 8 and ending at index 2
reverse_slice = my_list[8:1:-1]
print(reverse_slice)  # Output: [9, 8, 7, 6, 5, 4, 3]

# Note that if you use a positive step with a start and end index, you need to make sure that the start index is less than the end index, otherwise you'll get an empty list. For example:

# This will result in an empty list
empty_slice = my_list[2:5:1]
print(empty_slice)  # Output: []

# This will work as expected, slicing from index 5 to index 2
reverse_slice = my_list[5:2:-1]
print(reverse_slice)  # Output: [6, 5, 4]

# Get elements of the list in reverse order, skipping every other element
slice9 = my_list[::-2]
print(slice9)  # Output: [10, 8, 6, 4, 2]

# Note that if you use a negative step with a start and end index, you need to make sure that the start index is greater than the end index, otherwise you'll get an empty list. For example:

# This will result in an empty list
empty_slice = my_list[5:2:-1]
print(empty_slice)  # Output: []

# This will work as expected, slicing in reverse order from index 5 to index 2
reverse_slice = my_list[5:2:-2]
print(reverse_slice)  # Output: [6, 4]
slice1 = my_list[1:5]
print(slice1)  # Output: [2, 3, 4, 5]
# Get the last two elements of the list
slice2 = my_list[-2:]
print(slice2)  # Output: [9, 10]
# Get the first seven elements, skipping every third element
slice3 = my_list[:7:3]
print(slice3)  # Output: [1, 4, 7]
# Get the even-indexed elements of the list
slice4 = my_list[::2]
print(slice4)  # Output: [1, 3, 5, 7, 9]
# Get the odd-indexed elements of the list
slice5 = my_list[1::2]
print(slice5)  # Output: [2, 4, 6, 8, 10]
# Reverse the order of the list
slice6 = my_list[::-1]
print(slice6)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# Get the last three elements of the list, in reverse order
slice7 = my_list[-1:-4:-1]
print(slice7)  # Output: [10, 9, 8]
# Get the elements of the list in groups of three
slice8 = [my_list[i:i+3] for i in range(0, len(my_list), 3)]
print(slice8)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]}}}
# python in keyword{{{
# In Python, the in keyword is used to check whether a value is present in a sequence (such as a string, list, tuple, or set). It returns a boolean value (True or False) based on whether the value exists in the sequence or not.


# Here are a few examples to demonstrate the usage of the in keyword:

sentence = "The quick brown fox jumps over the lazy dog"
print("fox" in sentence)  # Output: True
print("cat" in sentence)  # Output: False
# numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True
print(6 in numbers)  # Output: False
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)  # Output: True
print("grape" in fruits)   # Output: False
# The in keyword is a useful tool for conditionally checking the presence of a value in a sequence, allowing you to make decisions or perform actions based on the result.}}}
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
# Note: As a result of the example above, the list will now contain 4 items.# #}}}
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
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']# #}}}
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
# []# #}}}
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
 # cherry# #}}}
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
# sort()	Sorts the list# #}}}
# #}}}

# python strings # {{{
# Ordered
# Immutable
# Homogeneous (only store character data)
# Accessed using index [] or slice []


# string immutability{{{
 # in Python, you can reassign a new value to a variable that holds a string. However, the immutability of strings refers to the fact that individual characters within a string cannot be modified directly.

# Here's an example to clarify this:
message = "Hello, World!"
message = "Hi there!"
# In the above code, the variable message initially holds the string "Hello, World!". However, when we reassign a new value to message using the statement message = "Hi there!", we are actually creating a new string object and assigning it to the variable message. The original string "Hello, World!" is not modified but replaced entirely.

# This behavior is different from mutable objects like lists, where individual elements can be modified directly without creating a new object.

# To illustrate the immutability of strings further:

message = "Hello"
message[0] = "J"  # This will raise a TypeError
# In the above code, trying to modify the first character of the string message using message[0] = "J" will result in a TypeError. This error occurs because strings do not support item assignment, and individual characters cannot be changed directly.

# So, while you can reassign a new value to a string variable, you cannot modify individual characters within the string. This is what is meant by the immutability of strings in Python.
#}}}
# Python Strings# {{{
# You can display a string literal with the print() function:
#You can use double or single quotes:
print("Hello")
print('Hello')
# Hello
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
# No, 'expensive' is NOT present.# #}}}
# Modify Strings methods{{{
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

a = "Hello, World!"
print(a.replace("Hello", "asdf"))
# asdf, World!

# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
b = a.split(",")
print(b)
# ['Hello', ' World!']# 


#}}}
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
# Hello World# #}}}
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
# zfill()	Fills the string with a specified number of 0 values at the beginning# #}}}
# #}}}

# dictionaries  {{{
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
#}}}
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
# Yes, 'model' is one of the keys in the thisdict dictionary# 

# Check if a value exists in the dictionary
my_dict = {"apple": 2, "banana": 4, "orange": 6}
if 4 in my_dict.values():
    print("4 exists in the dictionary")
else:
    print("4 does not exist in the dictionary")
# 4 does exists in the dictionary
# You can also use the not in keyword to check if a value does not exist in a dictionary. Here's an example:
if 8 not in my_dict.values():
    print("8 does not exist in the dictionary")
else:
    print("8 exists in the dictionary")
#8 does not exist in the dictionary




#}}}
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
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}# #}}}
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
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}# #}}}
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

# #}}}
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
# year 1964# #}}}
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
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}# #}}}
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
# Tobias# #}}}
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
# # #}}}
# #}}}
# Python Tuples (immutable list, declare with ())<!----># {{{
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
# <class 'tuple'># #}}}
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
# Yes, 'apple' is in the fruits tuple# #}}}
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
# #}}}
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
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')#}}}
# Tuple Methods# {{{
# https://www.w3schools.com/python/python_tuples_methods.asp
# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found# #}}}
# #}}}

# python sets(list no duplicates, uses {}, access with in and not in){{{
# Unordered
# Don't allow duplicate elements
# Allow heterogeneous elements
# Changable
# Accessed using in and not in operators
# all items inside must be immutable


# Python Sets# {{{
# https://www.w3schools.com/python/python_sets.asp
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.


# Sets in Python can only contain immutable data types, which means that you cannot include mutable objects such as lists, dictionaries, or other sets as elements of a set. This is because mutable objects can be changed, and if a mutable object is used as an element of a set, it could potentially change and break the set.

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

# When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.# #}}}
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
# Once a set is created, you cannot change its items, but you can add new items.# #}}}
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
# {'banana', 'cherry', 'apple', 'orange', 'kiwi'}# #}}}
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

# You can add a tuple to a set in Python using the add() method or the update() method. Here's an example:
my_set = {(1, 2), (3, 4)}
new_tuple = (5, 6)
# Using the add() method to add a tuple to the set
my_set.add(new_tuple)
print(my_set)  # Output: {(1, 2), (3, 4), (5, 6)}
# Using the update() method to add a tuple to the set
my_set.update({(7, 8)})
print(my_set)  # Output: {(1, 2), (3, 4), (5, 6), (7, 8)}



#}}}
# Loop Sets# {{{
# https://www.w3schools.com/python/python_sets_loop.asp
# Loop Items
# You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
# banana
# apple
# cherry# #}}}
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
# update()	Update the set with the union of this set and others# #}}}
# #}}}
