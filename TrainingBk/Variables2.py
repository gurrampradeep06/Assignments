class Myclass:
    global i
    i = 10
    j = "j in Myclass"
    print("myclass")


if __name__ == "__main__":
    print("Execution Starts here")
    global i
    i =1
    print(i)
    obj1 = Myclass()
    #print(obj1.i)
    obj2 = Myclass()
    print(obj2.j)
    obj3 = obj2
    print(obj3.j)
    obj3.j = "Changed from obj3"
    obj1.j = "changes by obj 1"
    print(obj3.j)
    print(obj2.j)
    print(obj1.j)
    print(obj3.j)
    print(obj2.j)





i = 100

def method1():
    global i
    i = 199


