"""
Create student class with instance, class and static methods.
"""


class __Student:
    Student_Name = ""
    Student_id = ""
    Student_Address = ""
    Student_Collage = "CMR Institute of technology"
    Student_Dept = "Electronics and communication"

    def __init__(self, Student_Name, Student_id, Student_Address):
        self.Student_Name = Student_Name
        self.Student_id = Student_id
        self.Student_Address = Student_Address

    @staticmethod
    def StudentCollage():
        return "Electronics and communication"

    def StudentDept(self):
        return self.Student_Dept

    def StudentDetails(self):
        return self.Student_id, self.Student_Address, self.Student_Name


Student1 = __Student("Pradeep", "17R01A0475", "old alwal")
print(__Student.StudentCollage())

# creating a static method with static method function
__Student.StudentDept = staticmethod(__Student.Student_Dept)

print(__Student.StudentDept)
# printing student details
print("Details of the student with id : {0} \n Student name : {2} \n Student Address : {1}\n ".format(
    *Student1.StudentDetails()))
