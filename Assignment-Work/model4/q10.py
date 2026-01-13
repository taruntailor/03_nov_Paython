# • Write a Python program to write a list to a file.

my_list = ["Apple", "Banana", "Cherry", "Date"]

filename = "output.txt"

with open(filename, "w") as file:
    for item in my_list:
        file.write(item + "\n")  # Write each item on a new line

print(f"List has been written to {filename}")
