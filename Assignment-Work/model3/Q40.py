# Write a Python script to print a dictionary where the keys are
# numbersbetween 1 and 15.

my_dict = {}

for i in range(1, 16):
    my_dict[i] = i ** 2  

print("Dictionary with keys 1 to 15 and their squares:")
print(my_dict)
