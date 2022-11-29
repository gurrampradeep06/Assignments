"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

print(*[i for i in range(1000,3000+1) if i%2 == 0],sep = ",")