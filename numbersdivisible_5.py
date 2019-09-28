#Print  4 digit numbers divisible by 5
items=[]
lis=input("Enter the  binaray numbers seperated by space ")
lis=list(lis.split(","))
for x in lis:
    q = int(x,2)
    if not q%5:
        items.append(x)
print(','.join(items))
