
#Count the occurence of characters in the string and print in the form of dictionary

str1 = input("Enter the string:")
count=1
dict1 =[]
dict2 = {}
for i in str1:
    if i in dict1:
        dict2[i]+=1
    else:
        dict1.append(i)
        dict2[i]=1
print("Output dictionary:",dict2)
        
    
