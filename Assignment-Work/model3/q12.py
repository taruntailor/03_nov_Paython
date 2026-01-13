# Write a Python function that takes a list and returns a new list
# with uniqueelements of the first list.

def unice_list(lst):
    return list(set(lst))

number =[1,2,3,4,5]
print(unice_list(number))