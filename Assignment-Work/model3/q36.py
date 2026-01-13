# Write a Python script to check if a given key already
# exists in adictionary.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'London'}

key_to_check = 'age'

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
