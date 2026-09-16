# "Input :
# Write a Python program to sort Counter by value
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}

# Expected output :
#  [('Chemistry', 87), ('Physics', 83), ('Math', 81)]"

dict1 = {'Math':81, 'Physics':83, 'Chemistry':87}

result = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
print(result)