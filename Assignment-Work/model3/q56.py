# • How can you pick a random item from a range?


import random

numbers = range(1, 11) 

rand_num = random.choice(numbers)
print("Random number from range:", rand_num)
