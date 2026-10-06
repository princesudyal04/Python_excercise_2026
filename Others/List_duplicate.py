# Print the unique list from given list and also find get the list of duplicate items
# Input:
# list1 = [1,3,2,1,1,2,2,3,4,5,6,6,6,6,6]
# Output:
# Unique list:  [1, 3, 2, 4, 5, 6]
# Duplicate numbers:  [1, 2, 3, 6]

list1 = [1,3,2,1,1,2,2,3,4,5,6,6,6,6,6]

unique = []
duplicate = []

for i in list1:
    if i in unique:
        if i not in duplicate:
            duplicate.append(i)
    else:
        unique.append(i)
print("Unique list: ", unique)
print("Duplicate numbers: ",duplicate)


