x = 10       # integer
name = "Tarun"   # string
price = 99.99    # float
is_active = True # boolean


# Same value multiple variables me:
a = b = c = 10

# Different values ek line me:
x, y, z = 5, "Hello", 3.14

# print value 

name = "Tarun"
print(name)



# | Type    | Example           |
# | ------- | ----------------- |
# | int     | 10                |
# | float   | 3.14              |
# | string  | "Hello"           |
# | boolean | True/False        |
# | list    | [1, 2, 3]         |
# | tuple   | (1, 2, 3)         |
# | dict    | {"name": "Tarun"} |



# ✅ 20 Python Variables Interview Questions & Answers
# 1. What is a variable in Python?

# A variable is a container used to store data values in memory.

# 2. How do you create a variable in Python?
# x = 10
# name = "Tarun"

# 3. Does Python require variable type declaration?

# No. Python is dynamically typed, so type automatically assign hota hai.

# 4. How to check variable type?
# x = 10
# print(type(x))

# 5. What are variable naming rules?

# Starts with letter or underscore

# No spaces

# No special characters

# Case-sensitive

# 6. What is dynamic typing?

# Variable ka type runtime par decide hota hai, manually declare nahi karna hota.

# 7. Can we change data type of variable later?

# Yes.

# x = 10
# x = "Hello"

# 8. How to assign multiple values to multiple variables?
# a, b, c = 1, 2, 3

# 9. How to assign one value to multiple variables?
# a = b = c = 5

# 10. What is a constant in Python?

# Python me official constant nahi hote, par hum CAPITAL LETTERS me likhte hain:

# PI = 3.14

# 11. What is the difference between local and global variables?

# Local variable: function ke andar

# Global variable: function ke bahar

# 12. Example of global variable
# x = 50  # global

# def fun():
#     print(x)

# 13. Example of local variable
# def fun():
#     y = 10   # local
#     print(y)

# 14. How to use global variable inside function?
# x = 10

# def myfun():
#     global x
#     x = 20

# 15. What is variable scope?

# Scope means kahaan variable accessible hai

# Local Scope

# Global Scope

# Function Scope

# Module Scope

# 16. What is type casting in Python?

# Changing one type to another:

# x = int("10")
# y = float("5.5")

# 17. What is id() function?

# Returns memory address:

# a = 10
# print(id(a))

# 18. What is the difference between mutable and immutable variables?

# Mutable: change ho sakte — list, dict

# Immutable: change nahi ho sakte — int, float, string, tuple

# 19. Can we delete a variable?

# Yes, using del

# x = 10
# del x

# 20. What happens if you print a deleted variable?

# Error:

# NameError: name 'x' is not defined

