#List of all number which is not even
num=input("Enter the numbers seperated by comma")
num1=list(map(int,num.split(",")))
num1=[x for x in num1 if x%2!=0]
print("List of number after removing even number",num1)