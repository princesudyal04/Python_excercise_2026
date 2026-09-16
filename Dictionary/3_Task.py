# "Input :
# Write a Python program to sum all the items in a dictionary.

# Expected Output :
# 293

dict1 = {1:2,3:4,5:6,7:8,9:10}
sum = 0

for key,values in dict1.items():
    sum= key+values
print(sum)