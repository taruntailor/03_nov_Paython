#  Write python program that swap two number with temp
# variable andwithout temp variable.
# Input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping using temp variable
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
