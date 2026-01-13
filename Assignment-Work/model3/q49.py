#  Write a Python program to combine values in python list of
# dictionaries.Sample data: [{'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount':
# 750}]
# o Expected Output: Counter ({'item1': 1150, 'item2':
# 300}) Write a Python program to create a
# dictionary froma string.
# o Note: Track the count of the letters from the
# string.Sample string:
# 'w3resource'
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e':
# 2, 'o': 1}


from collections import Counter

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

combined = Counter()
for entry in data:
    combined[entry['item']] += entry['amount']

print("Combined Counter:", combined)
