print("Enter String 1 : ")
str1 = input()
print("Enter String 2 :" )
str2 = input()
print("Enter swap count : ")
count = int(input())

print("Output : ",str2[:count]+str1[count:],str1[:count]+str2[count:])
