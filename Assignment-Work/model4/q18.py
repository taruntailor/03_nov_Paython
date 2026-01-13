# Write python program that user to enter only odd numbers,
# else will raisean exception

class NotOddNumberError(Exception):
    """Exception raised when a number is not odd."""
    pass

try:
    num = int(input("Enter an odd number: "))
    
    if num % 2 == 0:
        raise NotOddNumberError(f"{num} is not an odd number!")
    else:
        print(f"Thank you! {num} is an odd number.")

except ValueError:
    print("Error: Please enter a valid integer.")

except NotOddNumberError as e:
    print("Error:", e)

finally:
    print("Program execution finished.")
