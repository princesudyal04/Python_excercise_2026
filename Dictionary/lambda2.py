dict1 = {'Math':81, 'Physics':83, 'Chemistry':87}

def values(x):
    return x[1]

sort = sorted(dict1.items(), key= values, reverse=True)
print(sort)