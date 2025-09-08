
nums = range(1, 11)
print(nums)

a = 0
for n in nums:
    if n == 5:
        a = n
        print(f"a에 {n}이/가 대입됨")
    print("변동없음")

print(a)

num = input("세종이오")
print(num)

num1 = int(input())
num2 = int(input())
num3 = int(input())

sum = num1 + num2 + num3
print(sum)

sum = 0
for _ in range(3):
    sum += int(input())

print(sum)

i = 0
sum = 0
while i < 3:
    sum += int(input())
    i += 1

print(sum)