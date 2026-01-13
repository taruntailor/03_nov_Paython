# Why Do You Use the Zip () Method in Python?
# Write a Python program to create and display all combinations
# of letters,selecting each letter from a different key in a
# dictionary.
# o Sample data: {'1': ['a','b'], '2': ['c','d']} o Expected Output:
# o ac ad bc bd

# The zip() function is used to combine two or more iterables (like lists, tuples) element-wise into pairs.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))
