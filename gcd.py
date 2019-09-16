# Greatest common factor
a=int(input("Enter the First number"))
b=int(input("Enter the second number"))

for i in range(1,min(a,b)):
    if (a%i==0 and b%i==0):
        gcd=i
print("Greatest Common factor",gcd)