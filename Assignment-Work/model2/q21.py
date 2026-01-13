# Write a Python function that takes a list of words and returns
# the length ofthe longest one

def longest_word_length(words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

# Example
words = ["python", "java", "programming", "c"]
print("Length of longest word:", longest_word_length(words))
