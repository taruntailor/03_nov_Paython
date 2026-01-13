# Write a Python program to check multiple keys exists in a
# dictionary

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'country': 'USA'
}

keys_to_check = ['name', 'age', 'gender']

all_exist = all(key in my_dict for key in keys_to_check)

existing_keys = [key for key in keys_to_check if key in my_dict]
missing_keys = [key for key in keys_to_check if key not in my_dict]

print("Do all keys exist?", all_exist)
print("Existing keys:", existing_keys)
print("Missing keys:", missing_keys)
