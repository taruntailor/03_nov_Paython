# Write a Python program to generate and print a list of first
# and last 5elements where the values are square of
# numbers between 1 and 30.


squares = [i**2 for i in range(1, 31)]

first5 = squares[:5]

last5 = squares[-5:]

print("First 5 elements:", first5)
print("Last 5 elements:", last5)
