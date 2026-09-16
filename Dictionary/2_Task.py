# Input :
# Write a Python program to print a dictionary in table format.

# Expected Output :
# C1 C2    C3                                                                                                      
# 1   5    9                                                                                                         
# 2   6    10                                                                                                        
# 3   7    11

dict1 = {"C1":[1,2,3],"C2":[5,6,7],"C3":[9,10,11]}

print(*dict1.keys())
for row in zip(dict1["C1"],dict1["C2"],dict1["C3"]):
    print(*row)