#str copy of given string
def string(str,n):
    result=""
    for i in range(n):
        result=result + "  " + str
    return result
str=input("Enter the string")
n=int(input("Enter the number of copy u want"))
print("Final String",string(str,n))
