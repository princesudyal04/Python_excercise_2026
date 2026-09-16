# Input : 
# Write a program to accept a string from the user and display characters that are present at an even index number

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str1 = input("Enter any string value:")
length= len(str1)

for i in range(length):
    if i%2 == 0:
        print(str1[i])
