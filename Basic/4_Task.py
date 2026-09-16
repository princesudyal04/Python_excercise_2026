# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("Output 1 when same:")
print("Given list:",numbers_x)

if numbers_x[0] == numbers_x[-1]:
    print("Result is True.")
else:
    print("Result is False")

print()
print("+"*20)
print()

print("Output 2 when different:")
print("Given list:",numbers_y)

if numbers_y[0] == numbers_y[-1]:
    print("Result is True.")
else:
    print("Result is False")