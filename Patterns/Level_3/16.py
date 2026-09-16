#     *
#    * *
#   *   *
#  *     *
# *********

num = 5

for i in range(1, num + 1):
    if i == 1:
        print(" " * (num - i) + "*")
    elif i == num:
        print("*" * (2 * i - 1))
    else:
        print(" " * (num - i) + "*" + " " * (2 * i - 3) + "*")