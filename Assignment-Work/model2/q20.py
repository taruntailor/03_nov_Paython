# Write a Python program to find the first appearance of the
# substring 'not' and 'poor' from a given string, if 'not' follows the
# 'poor', replace the whole'not'...'poor'substring with 'good'.
# Return the resulting string.


# Input from user
text = input("Enter a string: ")

# Find positions
not_pos = text.find("not")
poor_pos = text.find("poor")

# Check condition
if not_pos != -1 and poor_pos != -1 and poor_pos > not_pos:
    result = text[:not_pos] + "good" + text[poor_pos + 4:]
else:
    result = text

print("Result:", result)
