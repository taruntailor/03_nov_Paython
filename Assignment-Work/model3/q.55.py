#  How Many Basic Types Of Functions Are Available In Python?
# How can you pick a random item from a list or tuple?




# 1️⃣ Basic Types of Functions in Python
# | Type                                | Description                                            | Example                                                    |
# | ----------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
# | **1. Built-in Functions**           | Functions that come with Python by default.            | `len()`, `print()`, `sum()`, `type()`                      |
# | **2. User-defined Functions**       | Functions you define yourself using `def`.             | `def add(a, b): return a + b`                              |
# | **3. Anonymous (Lambda) Functions** | Small, unnamed functions defined using `lambda`.       | `square = lambda x: x**2`                                  |
# | **4. Recursive Functions**          | Functions that **call themselves** to solve a problem. | `def factorial(n): return 1 if n==0 else n*factorial(n-1)` |


# 2️⃣ Picking a Random Item from a List or Tuple

# Python has a built-in random module to select random elements.

# Example 1: Random Choice from a List
import random

my_list = [10, 20, 30, 40, 50]
item = random.choice(my_list)
print("Random item from list:", item)

# Example 2: Random Choice from a Tuple
my_tuple = ('apple', 'banana', 'cherry')
item = random.choice(my_tuple)
print("Random item from tuple:", item)


# ✅ Explanation:

# random.choice(seq) → returns a random element from any sequence (list, tuple, or string).

# Make sure to import random first.
