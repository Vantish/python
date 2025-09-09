def divide(n1, n2):
    assert type(n1) in (int,)
    assert type(n2) in (int,)
    if n2 == 0:
        print('나누는 수는 0이 될 수 없습니다!!')
        return
    else:
        print(n1 // n2)

divide(10, 2)
divide(10, 0)

def add(n1, n2):
    if type(n1) == str or type(n2) == str:
        print('문자는 카악퉷')
        return
    else:
        print(f'{n1} + {n2} = {n1 + n2}')

add(3, 4)
add(10, 20)
add(10, 'bb')

def isadult(age):
    assert type(age) in (int,)
    assert age > 0, '잘못된 입력입니다.'
    if age > 19:
        print('성인입니다.')
    else:
        print('미성년자 입니다.')
    return

isadult(20)
isadult(8)
# isadult(-1)

def info(name, age, gender = 'f'):
    if gender == 'm':
        print(f'{name}은/는 {age}살 남성입니다')
    else:
        print(f'{name}은/는 {age}살 여성입니다')

info('둘리', 10, 'm')
info('도우너', 8, 'f')
