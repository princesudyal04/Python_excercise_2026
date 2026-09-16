# *****
# *   *
# *   *
# *   *
# *****

num=5

for i in range(1,num+1):
    if i in [1,num]:
        print("*"*num)
    else:
        print("*"+" "*(num-2)+"*")