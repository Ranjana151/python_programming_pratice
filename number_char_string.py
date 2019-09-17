# Count number of character in string
dict={}
str=input("Enter the string")

for x in str:
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1
for(k,v) in dict.items():
    print(k,v)