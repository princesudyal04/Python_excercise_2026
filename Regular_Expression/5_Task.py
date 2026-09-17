# Input :
# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

# Expected Output :
# 21 Kamarajar Rd.

import re

str1 = "21 Kamarajar Road"
match = re.sub("Road","Rd.",str1)
print(match)