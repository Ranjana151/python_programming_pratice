def sum_digit(x):
    sum=0
    while(x>0):
        digit=x%10
        sum=sum +digit
        x=x//10
    print("Sum of digits is",sum)
    return
#Main function
a=int(input("Enter the Number"))
sum_digit(a)

