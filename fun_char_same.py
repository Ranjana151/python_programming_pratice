#Return true if first n character of both the string are same else return true
def string(str1,str2,n):
    for i in range(0,n):
        if(str1[i]==str2[i]):
            return True
        else:
            return False

#Main function
str1=input("Enter the first string")
str2=input("Enter the second string")
n=int(input("Enter the value"))
print(string(str1,str2,n))