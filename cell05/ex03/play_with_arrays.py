#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2, 22, 9, 48]
print(array)

array = list(set(array))
new_array = [x + 2 for x in array if x > 5]
print(new_array)




""" Remove Duplicates from the list using the set() Method

 This is the most popular way by which the duplicates are removed 
from the list is set() method. But the main and notable drawback 
of this approach is that the ordering of the element is lost in 
this particular method.   """