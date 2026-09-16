# Input :
# Print multiplication table form 1 to 10

for row in range(1, 11):
    for column in range(1, 11):
        print(column*row, end=" ")
    print()