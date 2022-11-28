i = 1

def method():
    #i = 9
    j = k = 10
    global i
    i = 100

    i = 10
    print(i,j,k,end='\n')
    return i,j,k

class MyClass:
    i = 10
    def method2(self):
        return i,"method2 in i class"

if __name__ == '__main__':
    print(method())

    obj1 = MyClass()
    obj2 = MyClass()
    print(obj1.i)


    x = y = z = 10




    print(x,y,z,sep="\n")


    """new lines"""
    print("A B C Declaration")
    A = B = C = 10
    C = 100
    A,B,C = 100,200,300

    A=B
    A = 1000
    B = A = C
    print(A,B,C)

    global i
    i = 109
    print(obj1.i)
    print(obj1.method2())
