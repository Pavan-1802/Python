class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_stud):
        self.name=name
        self.max_stud=max_stud
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_stud:
            self.students.append(student)
            return True
        return False
    
    def get_average(self):
        value=0
        for i in self.students:
            value+=i.grade
        return value / len(self.students)
    
s1=Student("Tim", 25, 95)
s2=Student("Bill", 25, 90)
s3=Student("Jill", 25, 98)
s4=Student("Ken", 25, 85)
s5=Student("Sarah", 25, 79)

c1=Course("Science",4)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s4)
print(c1.add_student(s5))
print(c1.add_student(s3))