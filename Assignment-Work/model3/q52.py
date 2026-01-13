# Write a Python function that checks whether a passed string is
# palindromeor not


def is_palindrome(s):
    """
    Check if the given string 's' is a palindrome.
    """
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

# Example usage
test_str = "Racecar"
if is_palindrome(test_str):
    print(f"'{test_str}' is a palindrome.")
else:
    print(f"'{test_str}' is not a palindrome.")
