# A B C D E
# F G H I J
# K L M N O
# P Q R S T

k=0
for i in range(1,5):
    for j in range(1,6):
        print(chr(65+k),end=" ")
        k+=1
    print()