"""
Write python function with following  arguments
1. Required arguments
2. Keyword arguments
3. Default arguments
4. Variable-length arguments
"""


def RequiredArgs(a,b,bool):
    print(a,b,bool)


def KeywordArgs(a,b,bool):
    print(a,b,bool)


def DefaultArgs(a=0, b=0, bool = False):
    print(a, b, bool)


"""def DefaultArgs():
    print("Method with no args")"""


def VarArgs(*args):
    for var in args:
        print(var)


DefaultArgs()
DefaultArgs()

VarArgs(1,2,3,4,5,6,7)

"""requried ags are opposite to the Default args, in default agrs passing 
vars is optional but in requried args passing value is necessary if not interpreter will through error"""

RequiredArgs(10,20,True)
"""RequiredArgs() # throughs error"""

a = 100
b = 200
c = True
KeywordArgs(a,b,c)





