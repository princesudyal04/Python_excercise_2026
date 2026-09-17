# Input :
# Write a Python program to remove all whitespaces from a string
# Original string: Python    Exercises  

# Expected Output :
# Without extra spaces: PythonExercises 

import re 

str1 = "Python    Exercises "

match = re.sub(r"\s","",str1)
print("Original string:",str1)
print("Without extra spaces:",match)