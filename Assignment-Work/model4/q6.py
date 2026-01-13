# Write a Python program to read a file line by line and store it
# into a list Write a Python program to read a file line by line
# store it into a variable


# File name
filename = "myfile.txt"

lines_list = []

with open(filename, "r") as file:
    for line in file:
        lines_list.append(line.strip())  

print("Lines stored in a list:")
print(lines_list)
