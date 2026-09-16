#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI

num= 5

for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range((2*i)-1):
        print(chr(65+j),end="")
    print()