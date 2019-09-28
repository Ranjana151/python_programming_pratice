# print numbers between 100 and 400 where all digit of a number is an even number
items=[]
for i  in range(100,400):
    s=str(i)
    if(int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print(','.join(items))
