# "Input :
# Write a Python program that accepts a string and calculate the number of digits and letters. 
# Sample Data : Python 3.2

# Expected Output :
# Letters 6
# Digits 2"

str1 = "Python 3.2"
letter = 0
digit = 0

for i in str1:
    if i.isalpha():
        letter+=1
    elif i.isdecimal():
        digit+=1
print("Letters:",letter)
print("Digit",digit)