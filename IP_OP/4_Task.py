# Input :
# Write all content of a given file into a new file by skipping line number 5
# line1
# line2
# line3
# line4
# line5
# line6
# line7

# Expected Output :
# line1
# line2
# line3
# line4
# line6
# line7

with open("test.txt","r+") as file:
    a= file.readlines()
    data = []
    for i in a:
        data.append(i.strip())

with open("write2.txt","w+") as file:
    for i in range(len(data)):
        if i ==4:
            continue
        else:
            file.write(f"{data[i]}\n")
