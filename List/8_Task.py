# "Input :
# Write a Python program to extend a list without append. 
# Sample data: [10, 20, 30]
# [40, 50, 60]

# Expected Output :
# [40, 50, 60, 10, 20, 30]"

list1 = [10, 20, 30]
list2 = [40, 50, 60]

list1[0:0] = [40, 50, 60]
print(list1)

