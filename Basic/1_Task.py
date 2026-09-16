num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

mult = num1*num2
sum  = num1+num2

if mult <= 1000:
    print("The result is",mult)
else:
    print("The result is",sum)