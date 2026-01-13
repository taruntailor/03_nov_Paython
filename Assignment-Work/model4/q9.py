# • Write a Python program to count the frequency of words in a file.

from collections import Counter
import string

filename = "myfile.txt"

with open(filename, "r") as file:
    text = file.read().lower()  

text = text.translate(str.maketrans('', '', string.punctuation))

words = text.split()

word_counts = Counter(words)

print("Word frequencies in the file:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
