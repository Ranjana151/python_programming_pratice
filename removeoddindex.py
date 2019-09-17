#Remove odd index in the word
str=input("Enter the string")
result=""
for x in range(0,len(str),2):
    result+=str[x]
print("Word after removing odd index",result)