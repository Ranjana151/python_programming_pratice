def common_number(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
    return result
# Main function
list1=input("Enter the values seperated seperated by space")
list2=input("Enter the values seperated seperated by space")
lis1=list1.split()
lis2=list2.split()
r=common_number(lis1,lis2)
if r:
    print(lis1 ,"and" ,lis2 ,"has at least one common member",r)
else:
    print(lis1,"and",lis2," has not common at least one member",r)
