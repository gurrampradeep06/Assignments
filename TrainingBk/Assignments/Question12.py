"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class Question12:
    def getString(self):
        print("Enter the string :")
        inpstr = input()
        return inpstr
    def printString(self,inpstr):
        temp = str()
        for i in inpstr:
            #print(i,chr(ord(i) - 32))
            temp += (chr((ord(i) - 32)))
        print("printing the string in upper case : ", temp)

        #captilizing using string function

        print("printing the string in upper case : ",inpstr.upper())

def test():
    obj = Question12()
    temp = obj.getString()

    print("printing the string in test function : ",temp)
    obj.printString(temp)

#driver code
test()

