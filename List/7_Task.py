# Input :
# Write a Python program to create a list of empty dictionaries

# Expectd Output :
# [{}, {}, {}, {}, {}]

list1 =[]
for i in range(5):
    list1.append(dict())
print(list1)