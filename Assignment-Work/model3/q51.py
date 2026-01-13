#  Write a Python function to check whether a number is in a given
# range Write a Python function to check whether a number is
# perfect or not.


def is_in_range(number, start, end):
    """
    Check if 'number' is within the range [start, end] (inclusive).
    """
    return start <= number <= end

# Example usage
num = 7
print(f"Is {num} in the range 1 to 10? {is_in_range(num, 1, 10)}")
