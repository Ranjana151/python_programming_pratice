#print a list after removing 0,2,4,5 index in the list
lis=input("Enter the elements in the list")
lis1=lis.split(",")
lis1=[x for(i,x) in enumerate(lis1) if i not in (0,2,4,5)]
print(lis1)

