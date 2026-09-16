# Input :
# Write a Python program to read a file line by line store it into an array

# Expected Output :
#  ['Append this text.Append this text.Append this text.\n', 'Append this text.\n
# ', 'Append this text.\n', 'Append this text.\n', 'Append this text.\n'] 

with open("read.txt","r") as file:
    print(file.readlines())

