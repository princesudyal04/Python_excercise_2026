#     *
#    **
#   ***
#  ****
# *****

num = int(input("Enter the number of rows:"))

for i in range(1,num):
    print(" "*(num-i),"*"*i)
print()