# "Input :
# Write a Python script to sort (ascending and descending) a dictionary by value
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Expected Output :
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}"

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def values(x):
    return x[1]

sort_ascending = sorted(dict1.items(), key=values)
sort_descinding = sorted(dict1.items(), key=values, reverse=True)
print("Dictionary in ascending order by value : ",sort_ascending)
print("Dictionary in descending order by value :", dict(sort_descinding))