from mod1 import *
from mod2 import *

def sub(a, b):
    return a - b

try:
    lis = [1, 2, 3]
    lis[3]
    # 4 / 0
except (IndexError, ZeroDivisionError) as e:
    print(e)


print('정상종료')

try:
    age = int(input())
except ValueError as e:
    print('사람의 나이가 정확하지 않습니다')
else:
    if age <= 18:
        print('입장 불가')
    else:
        print('입장 가능')

f = None

try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(e)
finally:
    if f == None:
        print('파일이 없습니다')
    else:
        print('파일을 닫았습니다')
        f.close()

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('fly')

a = Eagle()
a.fly()