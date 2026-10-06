
# Input
# list1 = ["apple","and","bannana","ball"]
# Output
# {'a': ['apple', 'and'], 'b': ['bannana', 'ball']}

list1 = ["apple","and","bannana","ball"]

dict1 ={}

for i in list1:
    key = i[0]
    if key not in dict1:
        dict1[key]=[i]
    else:
        dict1[key].append(i)
print(dict1)
     
     