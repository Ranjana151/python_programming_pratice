# print user name in reverse order
user=input("Enter your name")
user1=user.split()
user1.reverse()
print(user1)
print("Reversed Name is:")
for i in user1:
    print(i,end=" ")