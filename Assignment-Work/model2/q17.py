# Write a Python program to count the occurrences of each word
# in a givensentence


# Input from user
sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    word = word.lower()   # case-insensitive
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
print(freq)
