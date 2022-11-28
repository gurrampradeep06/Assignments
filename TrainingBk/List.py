l1 = [3,2,1,4,5,6,7,8]
print(l1)
l2 = l1
print(l2)

print(l2[0],"-> 1st element")
print(l2[-1],"-> Last element")
l2[0] = 100
print(l2[0],"-> 1st element")
print(l2[-1],"-> Last element")
print(l1,l2)
print(l2[3:10])
print(l2[3:6],"-> [inclusive,exclusive]")

print(l2[-7:-1])
#printing the elements in the list
for i in l1:
    print(i)
for i in range(0, len(l1)):
    print(l1[i],end = " ")

#Adding the items into list

l1[0] = 1000
l2[2:4] = ["hello","world"]

print(l2)
print(l1)

l1.insert(0,"new element inserted")
#l1.sort() --> not work between strs and ints
print(l1)
#sorting the list
l3 = list((7,5,3,2,1,534,6,564))
l3.sort()
l3.insert(-1,3.3)
print(l3)
l3.sort()
l3.insert(-1,complex(1,3))
print(l3)
# nit work ith complex -> l3.sort()
print(l3)

l3.append(999)
l3.append(101)
l3.append(l2)
print(l3)

l4 = [l3.append(i) for i in l2]
print(l3)
print(l4)

l5 = [1,2,3]+[1,3,4,5]
print(l5)

l6 =[1,]
l7 = []
#print(l6[1],"--> list l6")
print(len(l6),"--> len l6",len(l7),"--> len l7")


l6.extend(l1)
print(l6,l1)