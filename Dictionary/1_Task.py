# "Input :
# Write a Python program to sort a list alphabetically in a dictionary.

# Expected Output :
# {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}"

dict1 = {'n1': [1, 3, 2], 'n2': [5, 2, 1], 'n3': [4, 2, 3]}
print("Original dict:",dict1)

for values in dict1.values():
    values.sort()
print("Values sorted dict:",dict1)
    