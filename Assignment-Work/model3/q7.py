# Write a Python program to count the number of strings where
# the string length is 2 or more and the first and last character
# are same from a givenlist of strings


def count_Strings(lst):
    count =0
    for s in lst:
        if len (s)>=2  and s[0]==s[-1]:
            count +=1
    return count
list1 = ['abc', 'xyz', 'aba', '1221', 'aa', 'a']
result = count_Strings(list1)
print("Count:", result)