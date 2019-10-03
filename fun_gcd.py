def gcd(x,y):
    for i in range(1,(min(x,y)+1)):
        if(x%i==0 and y%i==0):
            gcd=i
    print(gcd)
    return gcd
#Main function
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
print("Greatest Common factor is",gcd(a,b))