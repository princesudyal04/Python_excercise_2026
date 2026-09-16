# "Input :
# Write a Python program to check whether an alphabet is a vowel or consonant

# Expected Output:
# Input a letter of the alphabet: k                                       
# k is a consonant"

vowels = ['a','e','i','o','u']

char = input("Enter a letter of the alphabet: ").lower()

if char in vowels:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant")