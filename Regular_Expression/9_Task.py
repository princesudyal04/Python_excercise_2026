# Input :
# Write a Python program to insert spaces between words starting with capital letters

# Expected Output :
# Python
# Python Exercises
# Python Exercises Practice Solution 

import re

str1 = "Python"
str2 = "PythonExercises"
str3 = "PythonExercisesPracticeSolution" 

match = re.sub(r'(?<!^)(?=[A-Z])', ' ',str3)
print(match)
match = re.sub(r'(?<!^)(?=[A-Z])', ' ',str2)
print(match)
match = re.sub(r'(?<!^)(?=[A-Z])', ' ',str1)
print(match)