# Input :
# Write a program to use string.format() method to format the following three variables as per the expected output
# Given:
# totalMoney = 1000
# quantity = 3
# price = 450

# Expected Output :
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price:.2f} dollars.")
print("I have {} dollars so I can buy {} football for {:.2f} dollars.".format(totalMoney,quantity,price))
print("I have %d dollars so I can buy %d football for %.2f dollars."%(totalMoney,quantity,price))
