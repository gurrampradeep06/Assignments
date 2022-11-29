"""
Write a program which accepts a sequence of comma-separated numbers from console and
generate a list and a tuple which contains every number.
"""

print("Enter the input : ")

list1 = list(map(int,input().split(",")))

print("Resultant output list is :",list1)
print("Resultant output tuple is :",tuple(list1))