# *
# **
# * *
# *  *
# *****

num = 5

for i in range(1,num+1):
    if i in [1,2,num]:
        print("*"*i)
    else:
        print("*" + " "*(i-2) + "*")