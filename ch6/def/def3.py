def func1(**temp):
    print(temp)

def info(**p):
    if type(p) == dict:
        for i, a in p.items():
            print(i, a)

info(name = '둘리', age = 10)
info(name = '도우너', age = 8, address = '서울')

def calc(**temp):
    if type(temp) == dict:
        for i in temp:
            print(i)


calc(apple = 1200, banana = 800, orange = 1500)

di = {}
def show_scores(dic = 0, **temp):
    if dic == 0:
        if type(temp) == dict:
            for i in temp.values():
                print(i)
    else:
        if type(temp) == dict:
            for i, a in temp.items():
                di[i] = a

show_scores(di, 철수 = 90, 영희 = 85, 민수 = 100)
print(di)

def show_population(**temp):
    if type(temp) == dict:
        for i, a in temp.items():
            print(i, a)

show_population(seoul = 950, busan = 340, incheon = 300)

def show_items(**temp):
    if type(temp) == dict:
        for i in temp:
            print(i)

show_items(milk = 2500, bread = 2000, egg = 3000)

def add_text(t1, t2):
    return t1 + ' ' + t2

tempstr = add_text('hello', 'world')
print(tempstr)

def filt(temp):
    templis = ['바보']
    for i in templis:
        if temp == i:
            return True
    
    return False

def say_nick(temp):
    if filt(temp) == True:
        print(f'{temp}은/는 심한말이라 필터링')
        return
    else:
        print(f'나의 별명은 {temp} 입니다.')

say_nick('짱구')
say_nick('바보')

def func2():
    a = 1
    b = 2
    c = 3
    return a, b, c

print(func2())

a = 1

def func(a):
    a = a + 1

func(a)
print(a)