class Question4:
    def multiples(self, inp1, inp2):
        output = list()
        for i in range(inp1, inp2 + 1):
            if i % 7 == 0 and i % 5 != 0:
                output.append(i)
        return output


print("enter the ranges: ")
print("Enter range 1 : ")
inp1 = int(input())
print("Enter range2 : ")
inp2 = int(input())
obj1 = Question4()
print("The values which are divisible by 7 and multiples of 5 are :", obj1.multiples(inp1, inp2))
