class Person:
    def eat(self):
        print('밥을 먹는다')
    
    def sleep(self):
        print('잠을 잔다')

class Student(Person):
    def study(self):
        print('공부를 했다')

class Teacher(Person):
    def teach(self):
        print('가르쳤다')

