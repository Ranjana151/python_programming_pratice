#Using recursion function print fibonaci
def fibonaci(n):
    if n<=1:
        return n
    else:
        return (fibonaci(n-1)+fibonaci(n-2))

#Main function
n=int(input("Enter the number of terms"))
if n<=0:
    print("Enter the positive Number")
else:
    print("fibonaci series")
    for i in range(n):
        print(fibonaci(i))