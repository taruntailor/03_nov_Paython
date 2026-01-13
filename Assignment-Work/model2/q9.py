# Write a Python program to sum of three given integers.
# However, if twovalues are equal sum will be zero.

# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check if any two values are equal
if a == b or b == c or a == c:
    total = 0
else:
    total = a + b + c

print("Sum =", total)
