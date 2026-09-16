# Write a Python program to get unique values from a list.

given_list = [10, 20, 30, 40, 20, 50, 60, 40]   

set1 = set(given_list)
unique_list = list(set1)
print("List of unique numbers:",unique_list)

unique_list1 =[]
for i in range(len(given_list)):
    if given_list[i] not in unique_list1:
        unique_list1.append(given_list[i])
print("List of unique numbers with for loop:",unique_list1)