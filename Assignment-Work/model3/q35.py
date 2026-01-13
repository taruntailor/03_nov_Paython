# Write a Python script to concatenate following dictionaries to
# create anew one.

# Define dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Concatenate dictionaries
new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

# Display the result
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Dictionary 3:", dict3)
print("Concatenated Dictionary:", new_dict)
