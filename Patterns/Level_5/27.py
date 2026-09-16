#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

num = 5
for i in range(1,num+1):
    print(" "*(num-i), end="")
    for j in range(i):
        print(chr(65+j),end="")
    for k in range(j):
        print(chr(65+((j-k)-1)),end="")
    print()