# Write a Python program to copy the contents of a file to another
# file.


my_list = ["Apple", "Banana", "Cherry", "Date"]

filename = "output.txt"

with open(filename, "w") as file:
    for item in my_list:
        file.write(item + "\n")  

print(f"List has been written to {filename}")
