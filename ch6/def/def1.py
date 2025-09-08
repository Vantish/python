def add(a1, a2):
    if type(a1) in (list, tuple, dict) and type(a2) not in (list, tuple, dict):
        return a1
    elif type(a2) in (list, tuple, dict) and type(a1) not in (list, tuple, dict):
        a2.append(a1)
        return a2
    else:
        return a1 + a2

a = [1,2,3]
b = [4,5,6,10]


print(add(a,b))
print(type(a))

def mul(b1, b2):
    assert type(b1) not in (dict,), "b1 인자는 dict 타입일 수 없습니다."
    assert type(b2) not in (dict,), "b2 인자는 dict 타입일 수 없습니다."
    if type(b1) in (list, tuple) and type(b2) not in (list, tuple):
        temp = []
        if type(b2) == str:
            for i in b1:
                i = i * len(b2)
                temp.append(i)
        else:
            for i in b1:
                i = i * b2
                temp.append(i)
        return temp
    elif type(b2) in (list, tuple) and type(b1) not in (list, tuple):
        temp = []
        if type(b1) == str:
            for i in b2:
                i = i * len(b1)
                temp.append(i)
        else:
            for i in b2:
                i = i * b1
                temp.append(i)
        return temp
    elif type(b1) in (list, tuple) and type(b2) in (list, tuple):
        temp = []
        if len(b1) != len(b2):
            if len(b1) > len(b2):
                count = 0
                for i in b2:
                    temp.append(b1[count] * b2[count])
                    count += 1
                while count < len(b1):
                    temp.insert(count, b1[count])
                    count += 1            
            elif len(b1) < len(b2):
                count = 0
                for i in b1:
                    temp.append(b1[count] * b2[count])
                    count += 1
                while count < len(b2):
                    temp.insert(count, b2[count])
                    count += 1
        else:
            count = 0
            for _ in b1:
                temp.append(b1[count] * b2[count])
                count += 1
        return temp
    else:
        return b1 * b2

print(mul(a,b))

def hello():
    print('하이')

hello()

result1 = add(3, 4)

def say():
    return 'hi'

say()