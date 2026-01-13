#  What is lambda function in python? What we call a function
# which isincomplete version of a function?


# A lambda function is a small anonymous function in Python that is defined using the lambda keyword.

# Anonymous means it does not have a name (though you can assign it to a variable).

# Lambda functions are usually short, single-expression functions.


# Regular function
def square(x):
    return x ** 2

print(square(5))  # Output: 25

# Lambda function
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # Output: 25
