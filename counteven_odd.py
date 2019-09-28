#Number of odd and even number
lis=input("Enter the number ")
lis=list(map(int,lis.split(",")))
count_even=0
count_odd=0
for number in lis:
    if number%2==0:
        count_even+=1
    else:
        count_odd+=1
print("Total even numbers",count_even)
print("Total odd numbers",count_odd)