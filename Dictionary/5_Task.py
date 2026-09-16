# "Input :
# Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}

# Expected output :
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}"

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None,'c4':"Yellow","c5":None}

for key,values in list(dict1.items()):
    if values == None:
        dict1.pop(key)
print(dict1)