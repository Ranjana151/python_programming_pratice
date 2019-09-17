#Count the occurrences of each word
lis=input("Enter the word seperated by comma")
lis1=lis.split(",")
dict={}
for x in lis1:
    if x  in dict:
        dict[x]+=1
    else:
        dict[x]=1
for k,v in dict.items():
    print(k,v)
