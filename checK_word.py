#check whether a specified value is in the list or not
lis=input("Enter the values seperated by comma")
lis1=list(lis.split(","))
value=input("Enter the value u want to check ")
for i in range(len(lis1)):
    if lis1[i]==value:
        print("Item is find")