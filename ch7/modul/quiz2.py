import include

print(round(4.6))
print(round(4.2))
print(round(4.47, 2))

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

t1 = ('a', 'b', 'c')
t2 = ('d', 'e', 'f')

print(list(zip(t1, t2)))

dt = include.datetime.datetime(2025, 9, 11, 12, 38, 00)
print(dt.date())
print(dt.time())

date_str = '20250911'
print(include.datetime.datetime.strptime(date_str, "%Y%m%d"))

lis1 = [3, 1, 7, 4]
print(max(lis1))

lis2 = [10, 2, 33, 25]
print(sorted(lis2))

lis3 = [5, 10, 15]
print(sum(lis3))

print(abs(-7))
print(abs(-3.14))

lis4 = ['hello', [1, 2, 3], 3.14]
for i in lis4:
    print(type(i))