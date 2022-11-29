"""
Write a Python program to create an array of 5 integers and Perform following operation on the array
1. Display the array items.
2. Insert element.
3. Remove element.
"""

array = [1,2,3,4,5]
#inserting a element

array.append(6)
array.insert(0,0)

print(array)

#removing a element

array.remove(6)
array.remove(1)
print(array)

array.pop()
array.pop(1)
print(array)
