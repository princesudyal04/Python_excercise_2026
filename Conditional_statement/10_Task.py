# Input :
# Write a Python program to create the multiplication table (from 1 to 10) of a number.

num = int(input("Enter a number to create a table:"))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")