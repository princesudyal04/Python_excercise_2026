#Print downward Half-Pyramid Pattern with Star (asterisk)

for i in range(5):
    for j in range(5,i,-1):
        print("*", end=" ")
    print()