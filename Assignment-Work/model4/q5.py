# • Write a Python program to read last n lines of a file.

filename = "mtfile.txt"

n = int(input("Enter the number of lines to read from the end: "))

with open(filename, "r") as file:
    lines = file.readlines()  

for line in lines[-n:]:
    print(line.strip())
