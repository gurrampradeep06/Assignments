#arithmatic operators (+,-,/,%,**,//)

print(10+10)
print(100/10)
print(10-10)
print(10*10)
print(10**2)
print(100//10)


#logical operators

print(True or True or True)
print(True or False)
print(False or False)

#----------------------
print(True and True and True)
print(True and False)
print(False and False)

#---------------------
print(not True)
print(not False)


#relational opreators

a = 10
b = 20
c = 30
d = 30
print("relational/comparision")
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(d == c)
print(a!=b)
print(c != d)

print("Membership operators")
class myclass:
    i = 0
    j = 0
    def __init__(self,inp):
        self.i = inp
    """def __init__(self,inp1,inp2):
        self.i = inp1
        self.j = inp2
        print("2 parameter constructor")"""


"""obj4 = myclass(10,20)"""
"""print(obj4)"""
obj1 = myclass(100)
print(obj1.i, "-> print Obj1 value")
obj2 = myclass(100)
obj3 = obj2
print(obj1 is obj2)
print(obj2 is obj3)

"""print(1 is 1)
print(1 is 2)
#print(1 is "hello")"""

i = "Hello"
j = "Hello"
print(i is j)
j = "Hello World"

str1 = str("pradeep")
str2 = str("pradeep")

print(i is j)
print(str1 is str2,"-> str objects")

str3 = str2
print(str3 is str2)
str3 = ""
print(str3 is str2)
print(1 is "Hello", "-> 1 with hello")


print(str2[0])
#-------------------------------
print("****************Membership operator********************")


"""print(1 in 1)"""
"""print(1 in "1234")"""
print('1' in "1234")
print(1 in [1,2,3,4])
print(1 in {1:"hello",2:"world"})
print(1 in {"hello":1, "world":2}) ## only cosiderng keys
print([1,2] in [1,2,3,4])
print([1,2] in [[1,2],[1,2,3]])


print("***************Not in operator*****************")
print('1' not in "1234")
print(1 not in [1,2,3,4])
print(1 not in {1:"hello",2:"world"})
print(1 not in {"hello":1, "world":2}) ## only cosiderng keys
print([1,2] not in [1,2,3,4])
print([1,2] not in [[1,2],[1,2,3]])

print("**********************Bitwise operator***************************")

print(6 & 7, "--> Bitwise And")
print(6 ^ 7, "--> Bitwise xor")
print(~7, "--> Bitwise not")
print(6 | 7, "--> Bitwise or")
print(6 & 7, "--> Bitwise And")
print(6 << 1, "--> Bitwise shift left")
print(6 >> 1, "--> Bitwise shift right")


print("******************  Assignment operator   *******************")
j = 0
for i in range(0,100):
    j += 1
print(j)

for i in range(0,10):
    j -= 1
print(j)

for i in range(0,5):
    j *= 2
print(j)

for i in range(0,4):
    j/=2
print(j)
for i in range(0,4):
    j//=2
print(j)

for i in range(0,10):
    j += 1
print(j)

for i in range(0,4):
    j**=2
print(j)
j = 100
for i in range(0,2):
    j //=2

print(j)

