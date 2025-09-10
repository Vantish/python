
class Animal:
    def eat(self):
        print('잡아먹기!')

class Dog(Animal):
    def eat(self):
        print('달려가서 잡아먹기!')
    
    def bark(self):
        print('컹컹왈왈 탕탕 그르르')

class Cat(Animal):
    def bark(self):
        print('나는 냐옹이다옹~')

d = Dog()
d.eat()
d.bark()
Animal.eat(d)

class Book:
    def read(self):
        print('책을 읽는다')
class EBook(Book):
    def down(self):
        print('전자책을 다운한다')

eb = EBook()
eb.read()
eb.down()

class Monster:
    def attack(self):
        print('기본공격')
class Slime:
    def attack(self):
        print('점프 몸박')
sl = Slime()
sl.attack()
Monster.attack(sl)

class Student:

    school = '청라고등학교'

    def __init__(self, id, name):
        self.student_id = id
        self.student_name = name

    def info(self):
        print(f"이름 : {self.student_name} 학교 : {self.school}")

    def changeschool(self, name):
        self.school = name

sss = Student(101, '이동원')
sss.info()