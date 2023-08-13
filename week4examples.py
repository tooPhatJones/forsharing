
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

# The __init__() Function{{{
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
# }}}
# Object Methods{{{
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
# }}}
# The self Parameter{{{
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
# }}}
# Delete Object Properties{{{
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
# }}}
# Delete Objects{{{
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
# }}}
#}}}
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

# Create a Child Class{{{
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
# }}}
# Add the __init__() Function{{{
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
# Mike Olsen}}}
# what if you dont call the parents class constructor{{{
# In Python, when you define a class that inherits from a parent class, it's generally recommended to call the parent class's constructor (also known as the initializer or __init__ method) in the child class's constructor. This ensures that the parent class's initialization logic is executed, setting up the object properly.

# However, if you choose not to call the parent constructor in the child class, the parent class's initialization logic will be skipped, and its attributes and behavior may not be properly initialized. This can lead to unexpected results or errors, depending on how the parent class is designed and what functionality it provides.

# Here's an example to demonstrate the consequences of not calling the parent constructor:
class ParentClass:
    def __init__(self):
        self.parent_attribute = "I am from the parent class"

    def parent_method(self):
        print("This is a method from the parent class")


class ChildClass(ParentClass):
    def __init__(self):
        self.child_attribute = "I am from the child class"

child_obj = ChildClass()
# In the code above, the ChildClass inherits from ParentClass. However, the ChildClass does not call the parent class's constructor. As a result, the parent_attribute from the parent class is not initialized in the child object. If you try to access child_obj.parent_attribute or call child_obj.parent_method(), it will result in an AttributeError because the attribute and method from the parent class were not properly set up.

# To avoid this issue, it's generally recommended to call the parent class's constructor explicitly in the child class's constructor using the super() function:
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the parent constructor
        self.child_attribute = "I am from the child class"
# In this updated code, the super().__init__() line ensures that the parent class's constructor is called before initializing the child class's attributes. This way, both the parent and child attributes will be properly set up, allowing access to the parent's attributes and methods from the child object.
# }}}
# Use the super() Function{{{
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
# }}}
# Add child specific Properties{{{
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
# }}}
# Add child specific Methods{{{
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
# Welcome Mike Olsen to the class of 2019}}}


# #}}}







# class example inherit.py{{{
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")


# }}}
# class example linked list 1.py{{{
# Open VS Code to the week4/ folder, and create a new file in that folder named linked_list1.py.
# Enter:
# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None
# This creates a Node class that contains a value and reference (link) to the next value, initially set to None. None is a special value in Python that explicitly denotes the intentional lack of any value. 
# Below this class definition, and without any indentation, add the following lines:
# head = Node("1st Node")
# head.next = Node("2nd Node")
# head.next.next = Node("3rd Node")

# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
# This instantiates an object of the Node class as the value for the variable named head.  
# Then it instantiates a second object of the Node class as the value for the head object's instance attribute head.next. This effectively creates a link from the first Node object to the second. 
# Then it instantiates a third object of the Node class as the value for the instance attribute head.next.next. This creates a link from the first Node object, to the second, to the third. 
# Then it prints the value stored for each Node object. 
# This demonstrates the creation of a basic linked list. 
# When run in your terminal, you should see this result:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)
print(head.next.value)
print(head.next.next.value)

# }}}
# class example linked list 2.py{{{
# Open VS Code to the week4/ folder, and make a copy of the linked_list1.py file.
# Rename this copy linked_list2.py.
# In this copy, delete all the print statements but keep the rest of the code.
# The print statements are an inefficient way of printing the linked list's contents. We will implement a better way.
# In their place, add this function: 
# def iter_linked_list(node):
    # while node is not None:
        # print(node.value)
        # node = node.next
# This while loop traverses the linked list from node to node, printing the value for each then moving on to the next.
# At the bottom of the file, add this line of code to call the new function after the Node objects have been created:
# iter_linked_list(head)
# Save and run your code. You should see the same result as in the previous exercise:


# Then, add one more Node object to the linked list. Add this code beneath where the first three Node objects are instantiated:
# head.next.next.next = Node("4th Node")
# Then save and run again. You should now see:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next


head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")
head.next.next.next = Node("4th Node")


iter_linked_list(head)
# }}}
# class example linked list 3.py{{{
# Open VS Code to the week4/ folder and make a copy of the linked_list2.py file. Rename this copy linked_list3.py.
# Delete all the code in this copy except for the Node class definition.
# Beneath it, add the following:
# class LinkedList:
    # def __init__(self):
        # self.head = None
# This creates a LinkedList class with a constructor method that initializes the self.head attribute value to None.
# We will next implement a method that allows us to add nodes to a LinkedList object of this class.
# Add this method to the LinkedList class:
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)
This method will allow a LinkedList object to instantiate a new Node object with a given value.
If the LinkedList object does not yet have any nodes, its head attribute will be empty. In that case, this newly created Node object will be assigned to the head, we'll print a confirmation message, and the method will return (end).
Otherwise, if there is already a head node, we traverse it until we get to the tail node, which is the first node that has a next attribute of None.
Then, we link the newly created node to that tail node, thereby making it the new tail node, and print a confirmation message.


Testing
Add the following code for testing your newly created class:
llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
Save and run the code in the linked_list3.py file. You should see this output:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
# }}}
# class example linked list 4.py{{{
# Open VS Code to the week4/ folder.
# In that folder, create a new file named linked_list4.py.
# In this file, first define a DoubleNode class that initializes the attributes of value, next, and prev:
# class DoubleNode:
    # def __init__(self, value):
        # self.value = value
        # self.next = None
        # self.prev = None
# Then implement a DoubleLinkedList class as follows:
# class DoublyLinkedList:
    # def __init__(self):
        # self.head = None
        # self.tail = None

    # def append(self, value):
        # new_node = DoubleNode(value)

        # if self.head is None:
            # self.head = new_node
            # self.tail = new_node
            # print("Head Node created:", self.head.value)
            # return

        # new_node.prev = self.tail
        # self.tail.next = new_node
        # self.tail = new_node
        # print("Appended new Node with value:", self.tail.value)


# dllist = DoublyLinkedList()
# dllist.append("First Node")
# What does this code do?
# The DoublyLinkedClass keeps references to both a head and a tail node, instead of only the head.
# We can traverse from the head node to the tail node using the next attribute.
# We can traverse from the tail node to the head node using the prev attribute.
# When we append a new node to the tail end of a DoublyLinkedList object, we update both the previous tail node's next attribute, and the new tail node's prev attribute, so that the link goes both ways.
# Finally, we use the DoublyLinkedList class to instantiate an object named dllist.
# We use this instance's append method to add its first node.
# Go to your terminal and enter the following command to run this file using the Python interactive shell mode:
# python -i linked_list4.py
# In the shell, the dllist object will already exist and contain a node, so we can interact with it as follows.
# Enter the following commands one at a time into the Python shell:
# dllist.head.value
# dllist.tail.value
# This should show you that the head and the tail have the same value of "First Node".
# Next, enter the following commands one at a time:
# dllist.append("Second Node")
# dllist.head.value
# dllist.tail.value
# This should show you that the tail has now been changed to hold the value "Second Node", whereas the head remains the same.
# Still in the shell, enter these commands one at a time:
# dllist.head.next.value
# dllist.tail.prev.value
# What do you think you should see? Compare the results with your expectations.
# Next, enter:
# dllist.head.prev.value
# dllist.tail.next.value
# These commands should result in errors saying that 'NoneType' object has no attribute value. You cannot look at the value of the prev attribute for the head, nor the next attribute for the tail, because they both point to None.
# Finally, enter the following commands into the shell:
# dllist.append("Third Node")
# dllist.tail.value
# dllist.tail.prev.value
# dllist.tail.prev.prev.value
# dllist.head.next.next.value
# What do you expect as the result of these commands? Again, compare your expectations with the output.
# When you are done trying commands in the Python interactive shell, remember you can type exit() or ctrl-z then enter to quit.
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)


dllist = DoublyLinkedList()
dllist.append("First Node")

# }}}
# class example stack1.py{{{
# Open VS Code to the week4/ folder.
# In that folder, create a new file named stack.py.
# Begin by defining a Linked List Node class:
# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None
# Then, define a Stack class:
# class Stack:
    # def __init__(self):
        # self.head = None
        # self.num_nodes = 0
# In the Stack class, add a push() method that uses the Node class as follows:
    # def push(self, value):
        # new_node = Node(value)

        # if self.head is not None:
            # new_node.next = self.head

        # self.head = new_node
        # self.num_nodes += 1
# Also in the Stack class, add a pop() method as follows:
    # def pop(self):
        # if self.head is None:
            # return None

        # pop_node = self.head.value
        # self.head = self.head.next
        # self.num_nodes -= 1
        # return pop_node
# Next, we will instantiate an object from the Stack class, push items to it, then run a few tests to make sure all went well:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print("Pass" if (stack.num_nodes == 5) else "Fail")
# stack.push(5)
# print("Pass" if (stack.num_nodes == 5) else "Fail")

# print("Pass" if (stack.pop() == 5) else "Fail")
# print("Pass" if (stack.pop() == 4) else "Fail")
# Save and run your code in the bash terminal (using the command python stack.py). The output should appear as follows:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def push(self, value):
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head

        self.head = new_node
        self.num_nodes += 1

    def pop(self):
        if self.head is None:
            return None

        pop_node = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return pop_node


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.num_nodes == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
# }}}
# class example stack2.py{{{
# Open VS Code to the week4/ folder, and add a new file there named stack2.py.
# Enter this code into the file:
# class Stack:
    # def __init__(self):
        # self.items = []
# This has defined a class called Stack that initializes an items attribute variable to an empty list.
# Next, you will add the methods push(), pop(), and size() to this class:
    # def push(self, value):
        # self.items.append(value)

    # def pop(self):
        # if self.size() == 0:
            # return None
        # return self.items.pop()

    # def size(self):
        # return len(self.items)
# These methods are wrappers around the built-in Python list methods called append() and pop(), and Python's built-in len() function. We use them here to push an item to the top of the stack, to pop an item off the end, and to find the size of the stack.


# Testing
# Let's test our Stack class.
# Below and outside of the class definition, add the following lines to instantiate an object of the Stack class named stack, then use its instance method push() to add 4 items to itself.
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# Then add the following code to test the push(), pop(), and size() methods further:
# print("Pass" if (stack.size() == 5) else "Fail")
# stack.push(5)
# print("Pass" if (stack.size() == 5) else "Fail")

# print("Pass" if (stack.pop() == 5) else "Fail")
# print("Pass" if (stack.pop() == 4) else "Fail")    
# Save and run this code. You should see this output:
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.size() == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.size() == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
# }}}
# class example queue1.py {{{
# Open VS Code to the week4/ folder, and create a new file there named queue1.py.
# In this file, implement a class for a singly linked list's Node:
# class Node:
    # def __init__(self, value):
        # self.value = value
        # self.next = None
# Begin implementing a Queue class with a constructor method as follows:
# (Note: the ". . ." below is standing in for the code you entered previously. You do not need to type it in)
# . . .

# class Queue:
    # def __init__(self):
        # self.head = None
        # self.tail = None
        # self.num_nodes = 0
# Add a method to return the size() of the Queue:
# . . .

    # def size(self):
        # return self.num_nodes
# Add the enqueue() method as follows:
# . . .

    # def enqueue(self, value):
        # new_node = Node(value)

        # if self.head is None:
            # # self.head = new_node
            # # self.tail = new_node
            # self.head = self.tail = new_node  # Same as above two lines
        # else:
            # self.tail.next = new_node
            # self.tail = new_node

        # self.num_nodes += 1
# Add the dequeue() method as follows:
# . . .

    # def dequeue(self):
        # if self.head is None:
            # return None

        # # dequeue_node = self.head.value
        # dequeue_node_value = self.head.value
        # self.head = self.head.next
        # self.num_nodes -= 1
        # return dequeue_node_value
# Add these lines to instantiate an object from the Queue class and test it. Make sure these lines are not indented:
# q = Queue()
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')

# print("Pass" if (q.size() == 3) else "Fail")
# q.enqueue(4)
# print("Pass" if (q.size() == 4) else "Fail")

# print("Pass" if (q.dequeue() == 'a') else "Fail")
# print("Pass" if (q.dequeue() == 'd') else "Fail")
# print("Pass" if (q.size() == 2) else "Fail")
# Save and run your code. The output should be as follows:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node    # Same as above two lines
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:
            return None

        dequeue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
# }}}
#class example queue2.py# {{{
# Open VS Code to the week4/ folder, and create a new file there named queue2.py.
# The Queue class can easily be implemented using a Python list's built-in methods.
# Begin by defining the class and setting its items attribute to an empty list:
# class Queue:
    # def __init__(self):
        # self.items = []
# Then define its size(), enqueue(), dequeue(), and show_queue() methods as follows:
    # def size(self):
        # return len(self.items)

    # def enqueue(self, item):
        # self.items.append(item)

    # def dequeue(self):
        # if self.size() == 0:
            # return None
        # return self.items.pop(0)

    # def show_queue(self):
        # print(self.items)
# These use Python's built-in len() and print() functions, along with the append() and pop() list methods, to accomplish their purpose.
# Next, instantiate an object of the Queue class and test that it works as intended:
# q = Queue()
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')

# print("Pass" if (q.size() == 3) else "Fail")
# q.enqueue('d')
# print("Pass" if (q.size() == 4) else "Fail")

# print("Pass" if (q.dequeue() == 'a') else "Fail")
# print("Pass" if (q.dequeue() == 'd') else "Fail")
# print("Pass" if (q.size() == 2) else "Fail")
# q.show_queue()
# When you run the code above, you should see this output:


# Make sure you understand why this output is shown as a result of the provided code.
# If it does not make sense to you, and you have tried for 20 minutes, please reach out to your learning community in the chat server.
class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
q.show_queue()

# }}}
# class example using classes1.py{{{
# class Player:
  # max_hp = 4000


# player1 = Player()
# print(player1.max_hp)
# player2 = Player()
# print(player2.max_hp)

# Player.max_hp = 5000
# print(player1.max_hp)
# print(player2.max_hp)


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)
# player1.hp += 500
# player1.score += 10
# print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
# print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score) 
# }}}
# class example using classes2.py{{{
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_password("bestpassword")

# }}}


# Code Challenge: Linked List Prepend Method{{{
# Completion requirements
# View Make forum posts: 1
# Instructions
# Make a copy of the file linked_list3.py that you created in the module Exercise: Linked List Class. 
# You can give it any name you like, such as cc_linked_list.py.


# Your Challenge:
# Add a method called prepend() to the LinkedList class, with two parameters: self and value. 
# The following two instructions can be handled in an identical way as in the append() method:
# This method should instantiate a new object of the Node class, using the value passed in.
# If the self object does not have a head attribute, assign the new Node object you just instantiated as the head, and print the message "Head Node created: " followed by the value of the node.
# For the case in which the self object already has a head Node, you will then write code to assign the new Node object as the new head.
# The existing head must then be linked to the new head. 
# Afterward, print the message "Prepended new Head Node with value:" followed by the new head node's value.
# Also print the message "Node following Head is:" followed by the value of the node referenced by the new head node's next attribute.

# Testing
# The linked_list3.py file that you copied should have these lines at the bottom already, from the exercise that it was copied from:
# llist = LinkedList()
# llist.append("First Node")
# llist.append("Second Node")
# llist.append("Third Node")
# Delete the three lines that test the append() method, leaving only the first of the lines above. 
# Replace them with these lines:
# llist.prepend("First Node")
# llist.prepend("Inserted New First Node")
# Save and run your file. You should see this output, which shows that you were able to create a head (first) node with the prepend() method on an empty LinkedList object, then you were able to prepend a new head node that is linked to the previous head node:


# Answer to Code Challenge: Linked List Prepend Method (Instructors Only)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        new_node.next = self.head
        self.head = new_node
        print("Prepended new Head Node with value:", self.head.value)
        print("Node following Head is:", self.head.next.value)

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")# }}}
# Code Challenge: Ice Cream Shop Order Queue{{{
# Completion requirements
# View Make forum posts: 1
# Instructions
# Make a copy of the file queue2.py that you created in the module Exercise: Implementing a Queue as a List. You can give it any name you like, such as cc_order_queue.py.
# Delete all the code in it except for the entire Queue class definition. 

# Your Challenge:
# Below the Queue class definition, define another class named IceCreamShop as follows:
# class IceCreamShop:
    # def __init__(self, flavors):
        # self.flavors = flavors
        # self.orders = Queue()
# You will write three methods for this class: take_order(), show_all_orders(), and next_order().
# For the take_order() method, you will pass in 3 arguments aside from self: customer, flavor, and scoops. 
# Assume that the customer and flavor arguments will be strings, and scoops will be an integer.
# Write code to validate that the flavor string passed in exists in the self.flavors list, and that the scoops integer is between 1 and 3 inclusive, and show an appropriate error message if not.
# Assuming validation went well and we have a valid order, print "Order created!".
# Declare a variable named order. Assign as its value a dictionary that contains three keys, "customer", "flavor", and "scoops". For their values, use the arguments that were passed. 
# Enqueue this order dictionary to the self.orders queue. 
# For the show_all_orders() method, print all orders in the self.orders queue in a formatted way. See the Testing section below for the format. (Tip: You can use a for loop to format the orders as shown.)
# For the next_order() method, dequeue the head order in the queue and show it. See the Testing section below for the format. 


# Testing
# Add the following testing code to the bottom of the file:
# shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
# shop.take_order("Zachary", "pistachio", 3)
# shop.take_order("Marcy", "mint chip", 1)
# shop.take_order("Leopold", "vanilla", 2)
# shop.take_order("Bruce", "rocky road", 0)
# shop.show_all_orders()
# shop.next_order()
# shop.show_all_orders()
# This test code creates an IceCreamShop instance/object named shop using a list of ice cream flavors that is passed in.
# Then, it takes four orders. The first and second orders have valid values. The third and fourth orders do not (invalid flavor, then invalid number of scoops).
# Then, it shows all pending orders (the first and second). 
# Then, it dequeues and displays the next order that should be fulfilled (the first one in).
# Then, it shows all pending orders again (which should now have only one order left). 
# Save and run the code. The output should look like this:




# Answer to Code Challenge: Ice Scream Shop Order Queue (Instructors Only)
class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        if scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops")
            return
        print("Order created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        print("\nAll Pending Ice Cream Orders:")

        for order in self.orders.items:
            print("Customer:", order["customer"], "-- Flavor:",
                  order["flavor"], "-- Scoops:", order["scoops"])

    def next_order(self):
        print("\nNext Order Up!")
        order = self.orders.dequeue()
        print("Customer:", order["customer"], "-- Flavor:",
              order["flavor"], "-- Scoops:", order["scoops"])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
# }}}








