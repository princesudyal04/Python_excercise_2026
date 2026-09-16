#     1
#    121
#   12321
#  1234321
# 123454321
num=8
for i in range(1,num):
    print(" "*(num-i),end="")
    for j in range(1,i):
        print(f"{j}",end="")
    for k in range(1,i):
        if j-k!=0:
            print(f"{j-k}",end="")
    print()