# Write a Python program to returns sum of all divisors of a
# number

def sum_of_divisors(n):
    """
    Returns the sum of all divisors of n
    """
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

# Input from user
num = int(input("Enter a number: "))

# Calculate sum of divisors
result = sum_of_divisors(num)
print(f"Sum of all divisors of {num} is: {result}")
