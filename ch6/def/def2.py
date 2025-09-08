def add(a, b):
    print(a + b)

add(3, 4)

def hihello(name):
    print(f'{name}님, 환영합니다!')
hihello('둘리')

def customhello(name, word):
    print(f'{name}님, {word}')
customhello('또치', 'hi~~')

def hello(count = 3):
    for _ in range(count):
        print('안녕하세요')

hello(8)

def alladd(a1, a2):
    temp = 0
    for i in range(a1, a2 + 1):
        temp += i
    return temp

print(alladd(5, 10))

def sub(a1, a2):
    if a1 < a2:
        return -999
    else:
        return a1 - a2
print(sub(20, 10))
print(sub(10, 20))