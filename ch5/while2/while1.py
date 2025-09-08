# 반복문 없이 1부터 10까지 출력하세요
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

i = 0

while i < 10:
    print(i + 1)
    i += 1

print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")


i = 0
while i < 5:
    print("안녕하세요")
    i += 1


print("반가워요")
print("반가워요")
print("반가워요")

i = 0
while i < 3:
    print("반가워요")
    i += 1

print(2)
print(4)
print(6)
print(8)
print(10)

i = 0
while i < 5:
    print((i + 1) * 2)
    i += 1

i = 0
while i < 10:
    if (i + 1) % 2 == 1:
        i += 1
        continue

    print(i + 1)
    i += 1

print(3)
print(4)
print(5)
print(6)

i = 0
while i < 4:
    print(i + 3)
    i += 1

i = 0
while i < 5:
    print("hello")
    i += 1

i = 0
while i < 7:
    print(i)
    i += 1

i = 0
while i < 10:
    if (i + 1) % 2 == 0:
        i += 1
        continue

    print(i + 1)
    i += 1

i = 0
while i < 5:
    print((i + 1)+ i)
    i += 1

i = 0
while i < 10:
    print(i + 11)
    i += 1

i = 0
sub = 0
while i < 5:
    sub += (i+ 1)
    i += 1

print(sub)

nums = [10, 20, 30]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

i = 0
sub = 0
while i < 20:
    if sub >= 200:
        break
    sub += i + 1
    i += 1

print(sub)


lis = [100, 77, -5, 10]
i = 0
while i < len(lis):
    if lis[i] == -5:
        print(f"오류 : 해당 배열의 {i}번째 값이 {lis[i]}임")
        break
    print(lis[i])
    i += 1


i = 0
while i < 10:
    if (i + 1) % 3 == 0:
        break
    print(i + 1)
    i += 1

i = 0
lis = ['aa', 'bbb', 'ccccc', 'dd']
while i < len(lis):
    if len(lis[i]) > 4:
        break
    print(lis[i])
    i += 1

i = 0
while i < 10:
    if (i + 1) % 2 == 0:
        i += 1
        continue
    print(i + 1)
    i += 1

lis = [10, 'a', True, 20, 'b']
i = 0
while i < len(lis):
    if type(lis[i]) == int:
        i += 1
        continue
    print(lis[i])
    i += 1