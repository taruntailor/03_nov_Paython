# • Write a Python program to print all unique values in a dictionary.

# Sample dictionary
my_dict = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 200,
    'e': 100
}

# Get all unique values using set()
unique_values = set(my_dict.values())

# Print the unique values
print("Unique values in the dictionary:", unique_values)
