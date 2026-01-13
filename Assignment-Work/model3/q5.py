# Write a Python function to get the largest number, smallest
# num and sumof all from a list.


def list_info(lst):
    largest = max(lst)
    smallest = min(lst)
    total = sum(lst)
    return largest, smallest, total


# Example
numbers = [10, 20, 5, 40, 15]
result = list_info(numbers)

print("Largest number:", result[0])
print("Smallest number:", result[1])
print("Sum of all numbers:", result[2])
