# Input :
# Write a Python program to write a list to a file.

# Expected Output :
# Red                                                                                                           
# Green                                                                                                         
# White                                                                                                         
# Black                                                                                                         
# Pink                                                                                                          
# Yellow

list1 = ["Red","Green","White","Black","Pink","Yellow"]
with open("write.txt","w+") as file:
    for i in list1:
        file.writelines(f"{i}\n")
    
    
