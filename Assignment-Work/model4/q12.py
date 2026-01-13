#  Explain Exception handling? What is an Error in Python?


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Result is:", result)
finally:
    print("Execution finished.")
