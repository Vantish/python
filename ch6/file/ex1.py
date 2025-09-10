# aa = input('aa미만')
# bb = input('bb미만')
# print(int(aa) + int(bb))

def inputmul():
    temp1 = int(input('숫자만1'))
    temp2 = int(input('숫자만2'))
    return(temp1 * temp2)

def inputnameage():
    temp1 = input('이름1')
    temp2 = int(input('나이'))
    print(f'{temp1} 님의 나이는 {temp2}세 입니다.')

def penpineappleapplepen():
    temp1 = int(input('사과가격'))
    temp2 = int(input('사과개수'))
    return(temp1 * temp2)

# print(inputmul())
# inputnameage()
# print(penpineappleapplepen())

def ispass():
    temp1 = int(input('점수'))
    if temp1 >= 60:
        print('합격')
    else:
        print('불합격')

def buspay():
    temp1 = int(input('나이'))
    if temp1 > 0 and temp1 <= 12:
        print('1000원')
    elif temp1 > 12 and temp1 <= 18:
        print('1500원')
    else:
        print('2000원')

# ispass()
# buspay()

def rendom():
    while True:
        temp1 = input('반복문은 0이 아니면 멈추지 않아 Boy~')
        if temp1 == '0':
            break

# rendom()

value = '하이하이하이'
print(value, end = '따봉')

link = 'C:/Users/402/Desktop/ss/workspace/python/file/'

f = open('C:/Users/402/Desktop/ss/workspace/python/file/새파일.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    f.write(f'{i}\n')
f.close()

f = open('C:/Users/402/Desktop/ss/workspace/python/file/test.txt', 'w', encoding='utf-8')
f.write('hello\n')
f.write('hi')
f.close()

f = open('C:/Users/402/Desktop/ss/workspace/python/file/score.txt', 'w', encoding='utf-8')
f.write('80 90 70 100 60')
f.close()

f = open(link + 'numbers.txt', 'w', encoding='utf-8')
for i in range(10, 21):
    f.write(f'{i}\n')
f.close()

