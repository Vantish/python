mixed = [1, "apple", 3.14, True]

for val in mixed:
    print(val)

fruits = ["apple", "banana", "cherry"]
for val in fruits:
    print(val)

students = {"이름" : "둘리", "나이" : 20, "주소" : "인천"}
for val in students:
    print(val)

coffee_menu = {"아메리카노" : "2500원", "라떼" : "3000원", "케이크" : "4500원"}
for val in coffee_menu.values():
    print(val)


for i in range(11, 21):
    print(i)

for i in range(5, 16):
    print(i)

for _ in range(5):
    print("hi")

nums = [10, 20, 30, 40, 50]

sum = 0
for v in nums:
    sum += v

print(sum)

for n in range(1, 101):
    if n % 3 == 0:
        print(n)

sum = 0
for n in range(1, 101):
    if n % 3 == 0:
        sum += n
        print(sum)

'''
n = int(input())
v = ''
while n > 0:
    v += '*'
    n -= 1

print(v)
'''

'''
n = int(input())
v = ''
while n > 0:
    v += '*'
    print(v)
    n -= 1
'''

'''
n = int(input())
i = 0
a = 0
v = ''
while i < n:
    for _ in range(n + 1):
        if a < (n - i):
            v += ' '
            a += 1
        else:
            v += '*'
            a += 1
    print(v)
    i += 1
    v = ''
    a = 0
'''

'''
for i in range(int(input())):
    print(f"3 x {i + 1} = {3 * (i + 1)}")
'''

nums = [5, 9, 3, 8, 2]
answer = 0
for i in nums:
    if answer < i:
        answer = i
print(answer)

answer = 0
for i in range(1, 21):
    if answer > 100:
        break
    answer += i
print(answer)

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
