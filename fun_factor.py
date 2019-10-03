def factor(x):
    for i in range(1,x+1):
        if(x%i==0):
            print(i)
#Main Function
a=int(input("Enter the number for which u want find factors"))
factor(a)