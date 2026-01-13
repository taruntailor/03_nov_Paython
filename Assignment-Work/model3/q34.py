# Write a Python script to sort (ascending and descending) a
# dictionary byvalue.

my_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 5}

asc_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

desc_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order by Value:", asc_dict)
print("Descending Order by Value:", desc_dict)
