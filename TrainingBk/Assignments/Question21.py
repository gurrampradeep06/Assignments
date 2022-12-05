from TrainingBK.Question21_Import import MyException

try:
    print(10/0)
except:
    print("Divisor should be greater than 0")

arr = [1,2,3]
try:
    j = 0
    for i in range(0,10):
        print(arr[i])
except IndexError:
    print(i,"--> index failed ")
except:
    print("Except clause")
    print(i,"--> index failed ")
    print(j)

print(j)


try:
    for i in range(1,3):
        print(arr[i])
    print(100)

except IndentationError:
    print("check incantation")

try:
    print(100/0)
except:
    print("Divide by zero error")
finally:
    print("After statements")
    for i in range(1,10):
        print(i)


try:
    for i in range(10,-1,-1):
        print(100/i)
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally")

try:
    i = 1
    print(100/i)
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally")

try:
    i = 0
    print(100/i)
except:
    print("except block")
else:
    print("else block")
finally:
    print("finally")

try:
    i = 0
    print(100/i)
except:
    print("except block")
finally:
    print("finally")

try:
    i = 0
    print(100/i)
except:
    print("except block")
else:
    print("else block")



try:
    raise MyException("Custom Exception")
except:
    print("except block")


raise MyException("Custom Exception2")