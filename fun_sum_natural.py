#Sum of n natural number using recursion function
def Sum_Natural(n):
    if n<=1:
        return n
    else:
        return n + Sum_Natural(n-1)
#Main Function
n=int(input("Enter the number of terms u want to sum"))
if n<0:
    print("Enter the positive number")
else:
    print("Sum of", n ,"natural number is",Sum_Natural(n))