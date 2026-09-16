# Input :
# Write a Python program to compute the difference between two lists
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']

Color1 = ["red", "orange", "green", "blue", "white"]
Color2 = ["black", "yellow", "green", "blue"]

difference1 = list(set(Color1)-set(Color2)) 
print("Color1-Color1:",difference1)

difference2 = list(set(Color2)-set(Color1)) 
print("Color2-Color1:",difference2)
