print("Enter X value : ")
x = int(input())
print("Enter Y Value: ")
y = int(input())

list2d = list()
for i in range(0,x):
    templist = list()
    for j in range(0,y):
        templist.append(i*j)
    list2d.append(templist)

print(list2d)




