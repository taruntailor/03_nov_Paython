# Write a Python program to create a tuple with different data
# types.


mixed_tuple = (42, 3.14, "Hello, Python", True, None, [1, 2, 3], {"key": "value"})

print("Tuple:", mixed_tuple)
for item in mixed_tuple:
    print(item, "->", type(item))
