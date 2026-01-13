#  Write a Python program to unzip a list of tuples into individual
# lists


# Define a list of tuples
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

list1, list2 = zip(*list_of_tuples)

list1 = list(list1)
list2 = list(list2)

print("Original List of Tuples:", list_of_tuples)
print("First List:", list1)
print("Second List:", list2)
