# Input :
# Write a Python program to find sequences of lowercase letters joined with a underscore

# Expected Output :
# Found a match!                                                                                                
# Not matched!                                                                                                  
# Not matched!
import re

str1 = input("Enter an string: ")
match = re.findall(r"\b[a-z]+_[a-z]+\b",str1)
if bool(match):
    print("Found a match")
else:
    print("Not Matched")
