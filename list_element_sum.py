lis=input("Enter the comma seperated number")
list1=map(int,lis.split(","))
sum=0
for i in list1:
    sum=sum+i
print("Sum of all elements in the list ",sum)