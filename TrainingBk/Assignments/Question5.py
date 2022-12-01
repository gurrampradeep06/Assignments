"""
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers
as its input and print the numbers that are divisible by 5 in a comma separated sequence
"""


print("Enter comma sequence 4 digit binary numbers : ")
sequence = list(map(str,input().split(",")))
print("input sequence is : ",sequence)
outlistDec = list()
outlistBin = list()

for i in sequence:
    temp = 3;
    num = 0
    for j in i:
        num += int(j)*(2**temp)
        temp-=1
    if(num % 5 == 0):
        outlistDec.append(num)
        outlistBin.append(i)

print("the numbers which are divisible by 5 in Decimal is : ",*outlistDec)
print("the numbers which are divisible by 5 in Binary is : ",*outlistBin)

