# • What is the purpose continue statement in python?


# answer==>
# The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration only, and 
# immediately jump to the beginning of the next iteration of the loop . 

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
