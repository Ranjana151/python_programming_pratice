# Sum of three numbers if the value equal then it return thrice of the sum

def sum(x,y,z):
    sum=0
    if x==y==z:
        sum=(x+y+z)*3
    else:
        sum=x+y+z
    return sum
#Main Function
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
print("Sum is",sum(a,b,c))

