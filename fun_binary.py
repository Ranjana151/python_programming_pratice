# Convert decimal into binary
def binary(n):
    if(n>=1):
        binary(n//2)
        print(n%2,end=" ")

#Main program
n=int(input("Enter the integer"))
binary(n)