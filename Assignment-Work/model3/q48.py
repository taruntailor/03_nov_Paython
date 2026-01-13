# Write a Python program to find the highest 3 values in a
# dictionary


my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 150, 'e': 250}

top_3 = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3]

# Print the top 3 key-value pairs
print("Top 3 highest values:", top_3)
