#print list of words longer than a specific length
n=int(input("Enter the length of word"))
lis=input("Enter the element seperated by comma")
lis1=lis.split(",")
words=[]
for i in lis1:
    if len(i) >n:
        words.append(i)
print("Words are",words)