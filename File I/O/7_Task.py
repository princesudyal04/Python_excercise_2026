# Input :
# Write a Python program to copy the contents of a file to another file

# Expected Output :
# abc.py

with open("read.txt","r+") as file:
    list1 = file.readlines()
    data = "".join(list1)
    
with open("abc.txt","w+") as file:
    file.write(data)