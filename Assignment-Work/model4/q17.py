# How Do You Handle Exceptions With Try/Except/Finally In
# Python?Explain with coding snippets


# try:
#     # Code that might cause an exception
# except SomeException:
#     # Code to handle the exception
# finally:
#     # Code that always runs (cleanup, etc.)



try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
finally:
    print("This block always runs, cleaning up resources.")
