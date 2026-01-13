# • Write a Python program to read first n lines of a file.


filename = "myfile.txt"

n = int(input("Enter the number of lines to read: "))

with open(filename, "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break 
        print(line.strip())
