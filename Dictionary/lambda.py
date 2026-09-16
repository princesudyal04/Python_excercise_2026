list1 = ["chandigarh", "Mohali", "Delhi","Himachal","Jammu"]

def length(x):
    return len(x)

sort = sorted(list1, key=length)
print(sort)

sort2 = sorted(list1, key= lambda x: len(x))
print(sort2)