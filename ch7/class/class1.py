class Student:
    def __init__(self, id, name, grade):
        self.student_id = id
        self.student_name = name
        self.student_grade = grade

    def info(self):
        print(f"저는 {self.student_grade}학년 {self.student_name} 입니다")

stu1 = Student(1, '사람인', 2)
stu1.info()

stu2 = Student(2, '천지인', 4)
stu2.info()

print(stu2.student_grade)
print(stu2.student_id)
print(stu2.student_name)