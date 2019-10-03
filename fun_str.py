"""New string from old string where "Is" has been added to the front
if the old string not started with is then string remain unchanged """
def string(str):
    if str[:2]=="Is":
        return str
    else:
        return  "Is" + str 


str=input("Enter the string")
print("New String",string(str))
