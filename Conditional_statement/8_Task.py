# Input :
# Write a Python program to print the following patterns

# Expected output : 
#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
 
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 

for i in range(7):
    if i == 0:
        print("  ****")
    elif i in [1, 2]:
        print(" *")
    elif i == 3:
        print("  ***")
    elif i in [4, 5]:
        print("     *")
    else:
        print(" ****")

for i in range(15):
    if i in [0, 1, 2, 6, 7, 8, 12, 13, 14]:
        print("ooooooooooooooooo")
    elif i in [3,4,5]:
        print("oooo")
    else:
        print("             oooo")