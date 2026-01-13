# • Write a python program to find the longest words.

filename = "myfile.txt"

with open(filename, "r") as file:
    text = file.read()

words = text.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]

print("Longest word(s) in the file:", longest_words)
print("Length of the longest word:", max_length)
