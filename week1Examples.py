
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
# #}}}

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
x = memoryview(bytes(5))	#memoryview# #}}}
# Python Comparison Operators{{{
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
# }}}
# Operator Precedence{{{
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

# 5# #}}}

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



# #}}}
# Nested If{{{
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
# match statement(switch elsewhere){{{
# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks. This is superficially similar to a switch statement in C, Java or JavaScript (and many other languages), but it’s more similar to pattern matching in languages like Rust or Haskell. Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.

# The simplest form compares a subject value against one or more literals:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
# Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.

# You can combine several literals in a single pattern using | (“or”):

# case 401 | 403 | 404:
    # return "Not allowed"
# Patterns can look like unpacking assignments, and can be used to bind variables:

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
# Study that one carefully! The first pattern has two literals, and can be thought of as an extension of the literal pattern shown above. But the next two patterns combine a literal and a variable, and the variable binds a value from the subject (point). The fourth pattern captures two values, which makes it conceptually similar to the unpacking assignment (x, y) = point.

# If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables:

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
# You can use positional parameters with some builtin classes that provide an ordering for their attributes (e.g. dataclasses). You can also define a specific position for attributes in patterns by setting the __match_args__ special attribute in your classes. If it’s set to (“x”, “y”), the following patterns are all equivalent (and all bind the y attribute to the var variable):

Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
# A recommended way to read patterns is to look at them as an extended form of what you would put on the left of an assignment, to understand which variables would be set to what. Only the standalone names (like var above) are assigned to by a match statement. Dotted names (like foo.bar), attribute names (the x= and y= above) or class names (recognized by the “(…)” next to them like Point above) are never assigned to.

# Patterns can be arbitrarily nested. For example, if we have a short list of points, we could match it like this:

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
# We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block. Note that value capture happens before the guard is evaluated:

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
# Several other key features of this statement:

# Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. An important exception is that they don’t match iterators or strings.

# Sequence patterns support extended unpacking: [x, y, *rest] and (x, y, *rest) work similar to unpacking assignments. The name after * may also be _, so (x, y, *_) matches a sequence of at least two items without binding the remaining items.

# Mapping patterns: {"bandwidth": b, "latency": l} captures the "bandwidth" and "latency" values from a dictionary. Unlike sequence patterns, extra keys are ignored. An unpacking like **rest is also supported. (But **_ would be redundant, so it is not allowed.)

# Subpatterns may be captured using the as keyword:

# case (Point(x1, y1), Point(x2, y2) as p2): ...
# will capture the second element of the input as p2 (as long as the input is a sequence of two points)

# Most literals are compared by equality, however the singletons True, False and None are compared by identity.

# Patterns may use named constants. These must be dotted names to prevent them from being interpreted as capture variable:

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
# For a more detailed explanation and additional examples, you can look into PEP 636 which is written in a tutorial format.
# }}}

# indentation rules{{{
# there is no specific indentation level you need to use, but inside a code block, all indentation must be the same level. 
if 5 < 6:
    print("this is a valid indentation level")
    print("this is a valid indentation level")
if 5 < 6:
   print("this is a valid indentation level")
   print("this is a valid indentation level")
if 5 < 6:
  print("this is a valid indentation level")
  print("this is a valid indentation level")
if 5 < 6:
 print("this is a valid indentation level")
 print("this is a valid indentation level")

if 5 < 6:
print("this is not a valid indentation level")
print("this is not a valid indentation level")
if 5 < 6:
 print("this is a valid indentation level")
  print("this is not a valid indentation level")
   print("this is not a valid indentation level")
# }}}
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
# i is no longer less than 6#}}}
# all the places you can use the break and continue keywords :{{{
# You can use the break and continue keywords in Python in the following places
# break:

# In a for loop:
for i in range(10): 
    if i == 5: 
        break
    print(i)
# Prints 0 1 2 3 4
# In a while loop:
i = 0
while i < 10:
    if i == 5:
        break
    i += 1
    print(i)   
# # Prints 1 2 3 4

# In an if statement:
# if condition:
    # break

# In an else block of a for or while loop:
for i in range(10):
    pass
else:
    break
continue:

# In a for loop:
for i in range(10):
    if i % 2 == 0: 
        continue
    print(i)  
# Prints 1 3 5 7 9
# In a while loop:
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)    
# Prints 1 3 5 7 9
# In an if statement:
if condition:
    continue
# So in summary:

# break can be used to break out of the current loop or function
# continue can be used to skip the current iteration and continue with the next
# }}}
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
# #}}}
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
