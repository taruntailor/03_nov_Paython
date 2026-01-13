# • Write a Python program to find the second smallest 


def second_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    if len(unique_lst) >= 2:
        return unique_lst[1]
    else:
        return None  

# Example
numbers = [10, 20, 4, 45, 4, 20]
print("Second smallest number:", second_smallest(numbers))
