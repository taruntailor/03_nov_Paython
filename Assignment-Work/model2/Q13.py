# Write a Python program to count the number of characters
# (characterfrequency) in a string


text = input("Enter a string: ")

freq = {}
for ch in text:
    freq[ch] = text.count(ch)

print(freq)
