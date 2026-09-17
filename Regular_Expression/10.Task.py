# Input :
# Write a Python program to find all five characters long word in a string.

# Expected Output :
# ['quick', 'brown', 'jumps']

import re

str1 = "The quick brown fox jumps over the lazy dog"

match = re.findall(r'\b[a-zA-Z]{5}\b', str1)

print(match)