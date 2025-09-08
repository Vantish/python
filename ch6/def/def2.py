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

def isodd(num):
    assert type(num) in (int,), '숫자만 넣어주세요'
    if num % 2 == 0:
        print(f'{num} 숫자는 짝수입니다.')
    else:
        print(f'{num} 숫자는 홀수입니다.')

isodd(35)

def isstr(val):
    if type(val) == str:
        print(f'{val}은/는 문자입니다.')
    else:
        print(f'{val}은/는 문자가 아닙니다.')

isstr(58)

def isnegative(val):
    assert type(val) in (int,), '숫자만 넣어주세요'
    if val >= 0:
        print(f'{val}은/는 양수입니다.')
    else:
        print(f'{val}은/는 음수입니다.')

isnegative(32)

def firstval(lis):
    assert type(lis) in (list,), '리스트를 만들어 넣어주세요'
    return lis[0]

temp = [58, 4, 5]

print(firstval(temp))

def strlen(val):
    return len(val)

print(strlen('hi'))

def iszero(val):
    assert type(val) in (int,),'숫자가 아닙니다.'
    if val > 0:
        print(f'{val}은/는 양수입니다.')
    elif val == 0:
        print('0입니다.')
    else:
        print(f'{val}은/는 음수입니다.')

iszero(0)

def lisadd(lis):
    assert type(lis) in (list,), '리스트를 넣어주세요.'
    temp = 0
    for i in lis:
        temp += i
    return temp
print(lisadd([3, 6, 7]))

def 구구국(val):
    assert type(val) in (int,), '숫자를 넣어주세요.'
    for i in range(1, 10):
        print(f'{val} x {i} = {val * i}')

for i in range(2, 10):
    구구국(i)

def countstr(lis):
    assert type(lis) in (list,), '리스트를 넣어주세요.'
    temp = 0
    for i in lis:
        if type(i) == str:
            temp += 1
    return temp

test1 = [1, 'apple', 3.5, 'banana', 10, 'hi']
test2 = ['a', 'b', 'c']
test3 = [1, 2, 3]

print(countstr(test1))
print(countstr(test2))
print(countstr(test3))