# • Write a Python program to read a random line from a file.


import random

with open("sample.txt", "r") as file:
    lines = file.readlines()

random_line = random.choice(lines)

print("Random line from file:", random_line.strip())
