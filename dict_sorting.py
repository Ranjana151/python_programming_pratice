import collections
#dictionary sorting using values

d={1:"Abhishek",48:"Ujjwal",5:"Akshay",34:"Ranjana"}
sorted_d=sorted(d.items())
print("Dictionary after sorting in ascendng order",sorted_d)
sorted_d2=sorted(d.items(),reverse=True)
print("Dictionary after sorting in descending order",sorted_d2)
#dictionary sorting using key

od=collections.OrderedDict(sorted(d.items()))
print("Sorted dictionary using key",od)