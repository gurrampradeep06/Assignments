"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

print("Enter string 1 : ")
str1 = input()
print("Enter string 2 : ")
str2 = input()

temp1 = ""
temp2 = ""
for i in str1:
    if(i.isupper()):
        temp1 += i
    elif(i.islower()):
        temp1 += (chr((ord(i) - 32)))
    else:
        temp1 += i


for i in str2:
    if(i.isupper()):
        temp2 += i
    elif(i.islower()):
        temp2 += (chr((ord(i) - 32)))
    else:
        temp2 += i

print("The captilised string is : ",temp1)
print("The captilised string is : ",temp2)

##using string functions

print(str1.upper())
print(str2.upper())
