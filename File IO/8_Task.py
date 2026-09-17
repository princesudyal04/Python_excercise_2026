# Input :
# Write a Python program to assess if a file is closed or not

# Expected Output :
# False                                                                                                         
# True

file = open("read.txt","r+")

print(file.closed)

file.close()

print(file.closed)