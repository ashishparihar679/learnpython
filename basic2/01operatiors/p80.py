class Student:
    school = "ABC School"
    def __init__(self,student_name,mark):
        self.student_name=student_name
        self.mark=mark
    def display(self):
        print(f"The student name is {self.student_name} and mark is {self.mark} and scchool name is {self.school}")

s1=Student("Ashish",85)
s1.display()