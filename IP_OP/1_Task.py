# Input :
# Create a test.txt file and add the below content to it.

# Expected Output :
# line1
# line2
# line3
# line4

num = int(input("Enter the total no of line to be enter: "))

with open("test.txt","w+") as file:
    for i in range(1, num+1):
        file.write(f"line{i}\n")