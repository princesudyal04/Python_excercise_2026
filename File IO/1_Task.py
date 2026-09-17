# Input :
# Write a Python program to read first n lines of a file.

# Expected Output :                                                                                  
# Append this text.Append this text.Append this text.                                                           
# Append this text.                                                                                             
# Append this text.                                                                                             
# Append this text.                                                                                             
# Append this text.
n = int(input("Enter the number of lines you want to read:"))
with open("read.txt","r") as file:
    a=file.readlines()
    for i in a[:n]:
        print(i.strip())