# Input :
# Write a Python program to count the frequency of words in a file.

# Expected Output :
# Number of words in the file : Counter({'this': 7, 'Append': 5, 'text.': 5, 'text.Append': 2, 'Welcome': 1, 'to
# ': 1,})  
count = {}

with open("read.txt","r+") as file:
    data = file.readlines()
    list1 = []
    for i in data:
        list1.append(i.strip())
    str1 = " ".join(list1)
    list2 = str1.split()

    for word in list2:
        if word in count:
            count[word]+=1
        else:
            count[word] = 1
    print(count)

