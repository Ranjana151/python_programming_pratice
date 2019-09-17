# All even numbers from given numbers list in the same order and stop if 237 come in the list
lis=input("Enter the numbers seperated by comma")
lis1=list(map(int,lis.split(",")))
print(lis1)
print("Even numbers upto 237")
for x in lis1:
    if x==237:
        break
    else:
        if x%2==0:
            print(x)

