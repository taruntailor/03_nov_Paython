# • Write a python program to sum of the first n positive integers.

# Input from user
n = int(input("Enter a positive integer: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum of first", n, "positive integers is:", total)
