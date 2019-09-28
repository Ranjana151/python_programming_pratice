lines=[]
while True:
    l=input("Enter the line")
    if l:
        lines.append(l.lower())
    else:
        break
for l in lines:
    print(l)