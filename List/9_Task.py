# Input :
# Write a Python program to extract a given number of randomly selected elements from a given list. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]

# Expected Output :
# Selected 3 random numbers of the above list
# [4, 4, 1]

import random

list1 = [1, 1, 2, 3, 4, 4, 5, 1]
random_list = []

for i in range(3):
    random_list.append(random.choice(list1))
print(random_list)