a = 300
b = 200
c = 100

print(f"a는 {a}이고, b는 {b} 이며, c는 {c} 이다.")

lis = [ 'a', 'b', 'c', 'd', 'e' ]

for ch in lis:
    print(ch)

dic = { 'apple' : 1200, 'banana' : 800 , 'orange' : 1500 }

for i, a in dic.items():
    print(i, ':', a)

for i in range(20, 21):
    print(i)

for _ in range(3):
    print('하이')

scores = { '철수' : 80, '영희' : 95, '민수' : 70, '지연' : 100, '케리드라' : 100, '소상' : 20}

sub = 0
for i in scores.values():
    sub += i
print(f'점수의 평균은 {sub / len(scores)} 입니다.')

count = 0
for i in scores.values():
    if i >= 90:
        count += 1
print(f'90점 이상의 학생은 {count}명 입니다.')

nums = [1, 2, 3, 4]
lis = []
for i in nums:
    lis.append(i * 3)
print(lis)

lis2 = [n * 3 for n in nums]
print(lis2)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lis3 = []
for i in nums:
    if i % 2 == 0:
        lis3.append(i)
print(lis3)

lis4 = [i for i in nums if i % 2 == 0]
print(lis4)

strings = ['a', 'bb', 'ccc', 'dddd', 'e']
lis5 = []
for i in strings:
    if len(i) > 2:
        lis5.append(i.upper())
print(lis5)

lis6 = [i.upper() for i in strings if len(i) >= 2]
print(lis6)

짬통 = []
짬통.append(lis)
짬통.append(lis2)
짬통.append(lis3)
짬통.append(lis4)
짬통.append(lis5)
짬통.append(lis6)

print(짬통)



