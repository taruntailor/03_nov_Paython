# Write a Python program to get a string made of the first 2
# and the last 2chars from a given a string. If the string length
# is less than 2, return instead of the empty string.
# o Sample String: w3resource' o
# Expected Result: 'w3ce' o
# SampleString: 'w3' o Expected
# Result:
# 'w3w3' o Sample String: ' w' o
# Expected Result: Empty String



def string_mix(s):
    if len(s) < 2:
        return ""   # empty string
    else:
        return s[:2] + s[-2:]


# Test cases
print(string_mix("w3resource"))  
print(string_mix("w3"))          
print(string_mix("w"))           
