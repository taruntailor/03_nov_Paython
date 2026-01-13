# How many except statements can a try-except block have?
# Name Somebuilt-in exception classes:
# When will the else part of try-except-else be executed?
# • Can one block of except statements handle multiple exception?



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Enter a number.")
except Exception:  # catches any other exception
    print("Some other error occurred.")
