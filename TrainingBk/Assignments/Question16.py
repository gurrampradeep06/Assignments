"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""

print("Enter input string : ")
inpstr = input()
Alphabets = 0
nums = 0
for i in inpstr:
    if(i.isnumeric()):
        nums+=1
    elif(i.isalpha()):
        Alphabets+=1
    else:
        pass

print("Total count of Alphabets are :",Alphabets)
print("Total count of Alphabets are :",nums)