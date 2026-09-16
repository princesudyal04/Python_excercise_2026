# 123454321
#  1234321
#   12321
#    121
#     1

num=8

for i in range(num,0,-1):
    print(" "*(num-i),end="")
    for j in range(1,i):
        print(f"{j}",end="")
    for k in range(1,i):
        if j-k!=0:
            print(f"{j-k}",end="")
    print()