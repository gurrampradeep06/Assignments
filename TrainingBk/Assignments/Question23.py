class Collage:
    college_name = ""
    college_address = ""
    students = []
    def __init__(self, college_name, college_address):
        self.college_name = college_name
        self.college_address = college_address

    def Student(self, student_id, student_name):
        print(student_name, student_id)
        self.students.append((student_name,student_id))

print("Enter collage name : ")
college_name = input()
print("Enter collage aderss : ")
college_address = input()
institute1 = Collage(college_name,college_address)
institute1.Student("pradeep", 475)
institute1.Student("Vamshi", 455)
institute1.Student("Naresh", 476)
institute1.Student("Keshav", '4A2')

print(institute1.college_address)
print(*institute1.students,sep = "\n")


print("Enter collage name : ")
college_name = input()
print("Enter collage aderss : ")
college_address = input()
institute2 = Collage(college_name,college_address)


print(institute2.college_address,institute1.college_address)
print(institute2.college_name,institute1.college_name)
print("collage name",Collage.college_address)