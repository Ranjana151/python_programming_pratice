# Number is completely divisible by another number
def divisible(x,y):
    if(x%y==0):
        print("Number are completely divisible by another number")
        return
    else:
        print("Number are not completely divisible by another number")
        return
#Main function
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
divisible(a,b)