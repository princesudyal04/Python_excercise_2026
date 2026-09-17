# Input :
# Write a Python program to remove newline characters from a file

# Expected Output :
# [ 'Append this text.Append this text.Append this text.', 'Append this text.', 'Ap
# pend this text.', 'Append this text.', 'Append this text.']



with open("read.txt","r+") as file:
    data = file.readlines()
    list1 = []
    for i in data:
        list1.append(i.strip())
    print(list1)