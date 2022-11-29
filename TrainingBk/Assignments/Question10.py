"""
Write a program to convert list to set
"""

print("Enter the input : ")

list1 = list()
print("Enter Size of list : ")
for i in range(0,int(input())):
    print("Enter",i,"th Element : ")
    list1.append(input())

temp = set(list1)
list1 = temp

print("Resultant output set is :",list1)
