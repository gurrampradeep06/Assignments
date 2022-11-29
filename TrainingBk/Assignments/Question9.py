"""
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""

print("Enter the input :")

inplist = set(map(str,input().split(',')))

print("The unique sorted list is : ")
print(sorted(inplist))