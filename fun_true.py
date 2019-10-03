# Return True if two integer are equal or sum,difference equal to 5
def test(x,y):
    equ,sum,difference,no = False,False,False,False
    if x==y:
        equ=True
    elif(abs(x-y)==5):
        difference=True
    elif((x+y)==5):
        sum=True
    else:
        no=True
    return equ,sum,difference,no
# Main program
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
e,s,d,n=test(a,b)
if e:
    print("Numbers are equal")
elif s:
    print("Sum of two numbers are equal to 5")
elif d:
    print("Difference of two numbers are equal to 5")
elif n:
    print("Numbers are not equal ,sum or difference is also not equal to 5")


