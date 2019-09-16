# find number of vowels,constant,special char,digit
str=input("Enter the string")
vowels=constant=special_char=digit=0
for i in str:
    if i in 'aeiou':vowels+=1
    if i not in ('aeious' and '#@$&^*!' and '0123456789'):constant+=1
    if i in '0123456789':digit+=1
    if i in '#@$&^*!':special_char+=1


print("Number of vowels is:",vowels)
print("Number of constant is:",constant)
print("Number of digit is:",digit)
print("Number of special char is:",special_char)