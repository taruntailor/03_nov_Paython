# • Write a Python function to insert a string in the middle of a string.


def insert_string_middle(main_str, insert_str):
    mid = len(main_str) // 2
    return main_str[:mid] + insert_str + main_str[mid:]


# Example
print(insert_string_middle("Python", "is"))
print(insert_string_middle("<<>>", "Python"))
