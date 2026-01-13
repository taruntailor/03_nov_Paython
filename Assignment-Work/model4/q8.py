# Write a Python program to count the number of lines in a text
# file.

filename = "myfile.txt"

line_count = 0

with open(filename, "r") as file:
    for line in file:
        line_count += 1

print(f"The number of lines in the file is: {line_count}")
