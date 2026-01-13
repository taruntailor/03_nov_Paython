# Explain Inheritance in Python with an example? What is init? Or
# What IsA Constructor In Python?

#  Inheritance in Python?

# Inheritance is an OOP concept that allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).

# Purpose:

# Reuse code.

# Create a hierarchical relationship between classes.

# Types of inheritance in Python:

# Single inheritance

# Multiple inheritance

# Multilevel inheritance

# Hierarchical inheritance

# Hybrid inheritance


# What is __init__ in Python?

# __init__ is a special method in Python called a constructor.

# It is automatically called when an object is created.

# Used to initialize object attributes.



class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
student1 = Student("Alice", 20)
student1.display_info()
