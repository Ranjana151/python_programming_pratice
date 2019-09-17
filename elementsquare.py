#list of first and last 5 element and values are square of number between(1,30)
lis=input("Enter the numbers sepeated by space")
lis1=list(map(int,lis.split()))
number=[]
for i in range(1,31):
    x=i*i
    number.append(x)
print("Numbers are",number[0:5])
print("Numbers are",number[-5:-1])