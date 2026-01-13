# • Write a Python program to remove duplicates from a list.

lst = [10, 20, 10, 30, 20, 40, 50, 40]

uniqelist =[]

for i in lst:
    if i not in uniqelist:
        uniqelist.append(i)

print("list without duplicate", uniqelist)