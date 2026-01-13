# Write a Python program that will return true if the
# two givenintegervalues are equal or their sum or
# difference is 5.


# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Check conditions
if a == b or a + b == 5 or abs(a - b) == 5:
    print(True)
else:
    print(False)
