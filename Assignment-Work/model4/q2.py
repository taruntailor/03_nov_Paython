# • Write a Python program to read an entire text file.


# Open the file in read mode
with open("myfile.txt", "r") as file:
    content = file.read()

# Print the content
print("Content of the file:")
print(content)
