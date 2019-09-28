# filter out only odd numbers from list
old_list=[456,333,245,126]
print("Old list:",old_list )
new_list=list(filter(lambda x:x%2!=0,old_list))
print(new_list)