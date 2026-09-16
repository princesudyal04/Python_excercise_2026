# Input :
# Write a Python program to select the odd items of a list

# Expected Output :
# [1, 3, 5, 7, 9] 

list1 = [1,2,3,4,5,6,7,8,9,10]
odd_list = []

for i in list1:
    if i % 2 !=0:
        odd_list.append(i)
print("The list with odd elements is:",odd_list)