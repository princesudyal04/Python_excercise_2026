#     1
#    222
#   33333
#  4444444
# 555555555

num=5

for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1, 2*i):
        print(i,end="")
    print()