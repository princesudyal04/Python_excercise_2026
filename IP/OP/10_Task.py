# Write a program to check if the given file is empty or not


with open("abc.txt","r+") as file:
    current = file.read()
    if current == "":
        print("Empty")
    else:
        print("Not Empty")