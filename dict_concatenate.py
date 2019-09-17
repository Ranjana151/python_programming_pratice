#Concatenation of all dictionary
dict1={1:"ranjana",2:"sangam",3:"vandana"}
dict2={1:"red",5:"white"}
dict3={1:1,2:45}
d={}
for x in (dict1,dict2,dict3):
    d.update(x)
print("Concatenated dictionary are",d)