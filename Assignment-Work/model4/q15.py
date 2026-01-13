# • When is the finally block executed?
# ------------------------



# Always executes:

# Even if an exception occurs.

# Even if there is a return statement in try or except.

# Runs after try and except blocks:

# First, Python tries the try block.

# If an exception occurs, it runs the matching except block.

# Then, it always executes finally.


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run, cleaning up resources.")
