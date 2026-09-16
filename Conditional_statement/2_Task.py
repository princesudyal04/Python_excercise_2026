# Input :
# Write a Python program to construct the following pattern, using a nested for loop.

# Expected Output :
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(4):
    for j in range(4,i,-1):
        print("*",end=" ")
    print()