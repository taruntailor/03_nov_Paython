# # • How do you perform pattern matching in Python? Explain


# | Function                        | Description                                                 |
# | ------------------------------- | ----------------------------------------------------------- |
# | `re.match(pattern, string)`     | Checks for a match **only at the beginning** of the string. |
# | `re.search(pattern, string)`    | Searches **anywhere** in the string for the pattern.        |
# | `re.findall(pattern, string)`   | Returns **all non-overlapping matches** as a list.          |
# | `re.finditer(pattern, string)`  | Returns an **iterator** yielding match objects.             |
# | `re.sub(pattern, repl, string)` | **Replaces** matched patterns with `repl`.                  |
# | `re.split(pattern, string)`     | **Splits** a string at each match of the pattern.           |
