# Write a Python function to reverses a string if its length is a
# multiple of 4.

def reverse_if_multiple_of_4(text):
    if len(text) % 4 == 0:
        return text[::-1]
    else:
        return text

print(reverse_if_multiple_of_4("pyth"))     # python (length 6)

