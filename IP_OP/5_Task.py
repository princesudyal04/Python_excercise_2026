# Input :
# Accept a list of 5 float numbers as an input from the user

# Expected Output :
# [78.6, 78.6, 85.3, 1.2, 3.5]

list1 = []

for i in range(0,5):
    a = float(input(f"Enter the float number {i+1}: "))
    list1.append(a)
print(list1)