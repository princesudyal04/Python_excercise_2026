# "Input :
# Write a Python program to convert given a dictionary to a list of tuples.
# Original Dictionary:
# {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

# Expected Output :
# Convert the said dictionary to a list of tuples:
# [('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]"

dict1 = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
list1 = []

for key, values in dict1.items():
    list1.append((key,values))
print(list1)