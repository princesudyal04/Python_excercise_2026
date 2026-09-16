#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

num = 5

for i in range(1,num+1):
    if i==1:
        print(" "*(num-i) + "*")
    else:
        print(" "*(num-i) + "*" + " "*(2 * i -3) + "*")

for i in range(num-1,0,-1):
    if i==1:
        print(" "*(num-1) + "*")
    else:
        print(" "*(num-i) + "*" + " "*(2 * i -3) + "*")