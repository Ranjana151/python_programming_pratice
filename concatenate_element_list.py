# concatenate all the elements in the list

lis=input("Enter the elements seperated by comma")
lis1=lis.split(",")
result=""
for x in range(len(lis1)):
    result+=lis1[x]
print("Concatenate elements is",result)
