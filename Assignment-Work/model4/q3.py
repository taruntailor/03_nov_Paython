# Write a Python program to append text to a file and display the
# text.



# File name
filename = "myfile.txt"

# Append text to the file
with open(filename, "a") as file:
    file.write("\nThis is a new line added to the file.")

# Read and display the updated file content
with open(filename, "r") as file:
    content = file.read()

print("Updated content of the file:")
print(content)
