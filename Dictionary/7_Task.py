# "Input :
# Write a Python program to find the key of the maximum value in a dictionary
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

# Expected Output :
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')"

dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}

max_value = max(dict1, key=dict1.get)
min_value = min(dict1, key=dict1.get)

print("Max value key is:",max_value)
print("Min value key is:",min_value)

