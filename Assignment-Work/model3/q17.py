# number in a list.Write a Python program to get unique
# values from a list


numbers = [10, 20, 10, 30, 20, 40, 50, 40]

unice_value = []

for num in numbers :
    if num not in  unice_value:
        unice_value.append(num)
print(unice_value)