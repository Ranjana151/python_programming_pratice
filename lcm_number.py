# print lcm of two numbers
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
if x>y:
    z=x
else:
    z=y
while(True):
    if((z%x==0 and z%y==0)):
        Lcm=z
        break
print("Lcm of two number is",Lcm)
