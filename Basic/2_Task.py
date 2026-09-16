print("Printing current and previous number sum in a range(10)")

sum=0
a= 0

for i in range(10):
    a, b = i, a
    sum = a+b

    print(f"Current Number {a} Previous Number  {b}  Sum:  {sum}")



    
