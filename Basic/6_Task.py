#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

def exponent(base,power):
    output = base ** power
    return output

b = int(input("Enter the base value:"))
p = int(input("Enter the power value:"))

print(f"{b} raise to the power {p}:",exponent(2,5))