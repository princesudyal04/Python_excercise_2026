# Input :
# Write a program to take three names as input from a user in the single input() function call.

# Expected Output:
# Enter three string Emma Jessa Kelly
# Name1: Emma
# Name2: Jessa
# Name3: Kelly

def single_input():
    name1, name2, name3 = input("Enter three string ").split()
    return name1, name2, name3

name1, name2, name3 = single_input()
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)
