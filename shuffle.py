import random
lis=input("Enter the list seperated by comma")
list=lis.split(",")
random.shuffle(list)
print("List after shuffling",list)
