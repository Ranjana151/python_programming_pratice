str=input("Enter the string")
n=int(input("Enter the index which u want to remove"))
first_part=str[:n]
print(first_part)
last_part=str[n+1:]
print(last_part)
print(first_part + last_part)