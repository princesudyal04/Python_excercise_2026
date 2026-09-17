# Input :
# Write a Python program to do a case-insensitive string replacement
# Original Text:  PHP Exercises

# Expected Output :
# Using 'php' replace PHP
# New Text:  php Exercises
import re

str1 = "PHP Exercises"
match = re.sub(r"php","php",str1, flags=re.IGNORECASE)
print(match)