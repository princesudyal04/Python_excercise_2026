# "Input :
# Write a Python program that accepts a word from the user and reverse it.

# Expected Output :
# Input a word to reverse: ecruoser3w  
# w3resource"

str1 = input("Enter any string to be reverse:")
reverse_str = ""

for i in str1:
    reverse_str= i + reverse_str
print("Entered string is:",str1)
print("Reverse string is:",reverse_str)