# Input :
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

# Expected Output :
# True                                                                                                          
# False 
import re

str1 = input("Enter the string: ")

match = re.fullmatch(r"[a-zA-Z0-9]+",str1)
if bool(match):
    print(True)
else:
    print(False)


