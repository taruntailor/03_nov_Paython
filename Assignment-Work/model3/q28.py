# • Write a Python program to replace last value of tuples in a list.


list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_value = 100

updated_list = [t[:-1] + (new_value,) for t in list_of_tuples]

print("Original List:", list_of_tuples)
print("Updated List:", updated_list)
