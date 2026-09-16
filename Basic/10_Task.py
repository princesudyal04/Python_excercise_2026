# Input :
# Write a program to check if the given number is a palindrome number.

# Expected Output :
# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

num = int(input("Enter an integer to check if it is Pallindrome or not?: "))

actual_num = num
revese_num =0

while num>0:
    last_digit = num%10
    revese_num = revese_num*10 + last_digit
    num = num // 10

print("Original number is:",actual_num)
print("Reverse number is:",revese_num)

if actual_num == revese_num:
    print(f"Entered number {actual_num} is a pallindrome.")
else:
    print(f"Entered number {actual_num} is not pallindrome.")