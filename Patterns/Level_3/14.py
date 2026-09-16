# ********
# *      *
# *      *
# ********
num = 4
for i in range(1,num+1):
    if i in [1,num]:
        print("*"*(2*num))
    else:
        print("*" + " "*((2*num)-2) + "*")