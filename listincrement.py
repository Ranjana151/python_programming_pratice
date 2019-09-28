# lamda function to increment the items in list by 2 using map function
old_list=[23,34,45,36]
print("Old list is:",old_list)
new_list=list(map(lambda x:x+2,old_list))
print("New list",new_list)
