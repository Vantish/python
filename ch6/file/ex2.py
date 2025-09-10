link = 'C:/Users/402/Desktop/ss/workspace/python/ch6/file/'

f = open(link + 'score.txt', 'r')
lines = f.readline()
print(lines)
f.close()

f = open(link + 'score.txt', 'r')
text = f.read()
print(text)

lis = text.split(' ')
for a in lis:
    print(a)
f.close()

f = open(link + '새파일.txt', 'r')
temp = f.readlines()
print(temp)
for line in temp:
    print(line, end = '')
f.close()

f = open(link + '새파일2.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    f.write(f'{i}번째 줄 입니다.\n')
f.close()

f = open(link + '새파일2.txt', 'a', encoding='utf-8')
for i in range(11, 21):
    f.write(f'{i}번째 줄 입니다.\n')
f.close()

f = open(link + '새파일2.txt', 'r', encoding='utf-8')
lis = f.readlines()
for line in lis:
    print(line, end='')

f.close()