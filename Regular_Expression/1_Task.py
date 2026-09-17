# Input :
# Write a Python program to check for a number at the end of a string

# Expected Output :
# False                                                                                                         
# True

import re

str1 = input("Enter the string: ")

match = re.search(r"\d$",str1)
if match == None:
    print("Is the String Ends with digit? ",False)
else:
    print("Is the String Ends with digit? ",True)


