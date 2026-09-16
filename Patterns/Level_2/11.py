#     1
#    123
#   12345
#  1234567
# 123456789

num=5

for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1, 2*i):
        print(j,end="")
    print()