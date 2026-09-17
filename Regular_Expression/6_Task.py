# Input :
# Write a Python program to match if two words from a list of words starting with letter 'P'

# Expected Output :
# ('Python', 'PHP')
import re

list1 = ["Python","Print","Keyboard","Store","Pics"]
match_list = []

for i in list1:
    match = re.findall(r"^P.*",i)
    if bool(match):
        match_list.append(("".join(match)))
print(tuple(match_list))