# "Input :
# Write a Python program to get next day of a given date.
# Input a year: 2016                                                      
# Input a month [1-12]: 08                                                
# Input a day [1-31]: 23 

# Expected Output :
# The next date is [yyyy-mm-dd] 2016-8-24   "

year = int(input("Enter a year: "))
month = int(input("Enter a month [1-12]: "))
day  = int(input("Enter a day [1-31]: "))

if month > 12 or month < 1:
    print("Invalid month.")
else:
    if day >31 or day < 1:
            print("Invalid day.")
    else:
        if day == 31:
            day= 1
            month+=1
            if month==13:
                year+=1
                month=1
        else:
            day+=1
        print(f"The next date is [yyyy-mm-dd]: {year}-{month}-{day}")