# Input :
#  Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

# Expected Output :
# Not matched!                                                                                                  
# Not matched!                                                                                                  
# Found a match

import re

str1 = input("Enter the string: ")
match = re.search(r"a.*b$", str1)
if match == None:
    print("Not Matched !")
else:
    print("Found a match !")