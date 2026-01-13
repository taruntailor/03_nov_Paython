list_of_tuples = [(), (1, 2), (), (3, 4, 5), (), (6,)]

filtered_list = [t for t in list_of_tuples if t]

print("Original List:", list_of_tuples)
print("List after removing empty tuples:", filtered_list)
