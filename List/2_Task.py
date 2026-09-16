# Input :
# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# Sample list : ['p', 'q']
# n =5

# Expected output :
#  ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

list1 = ['p','q']
length = len(list1)

expected_list =[]
num =5

for i in range(1,num+1):
    for j in range(length):
        data = list1[j]+str(i)
        expected_list.append(data)
print(expected_list)