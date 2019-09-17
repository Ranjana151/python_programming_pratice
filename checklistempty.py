#print list is empty or not
#check again after some time

lis=input("Enter the element seperated by comma")
lis1=lis.split(",")
if not lis1:
    print("List is  empty")
else:
    print("List is not empty")