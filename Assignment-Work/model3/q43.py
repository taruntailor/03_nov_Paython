# Write a Python program to combine two dictionary adding
# values forcommon keys.
# o d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b':
# 200,’d’:400}

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}

for key, value in d1.items():
    combined_dict[key] = value

for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print("Combined dictionary:", combined_dict)
