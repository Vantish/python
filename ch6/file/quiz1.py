link = 'C:/Users/402/Desktop/ss/workspace/python/ch6/file/'

Q = open(link + 'score.txt', 'r')
lis = Q.read()
tempint = lis.split(' ')
temp = 0
count = 0
for i in tempint:
    temp += int(i)
    count += 1
    
print(temp / count)

Q.close()

Q = open(link + 'numbers.txt', 'r')
lis = Q.read()
tempint = lis.split('\n')
for i in tempint:
    if i == '':
        break
    else:
        if int(i) % 2 == 0:
            print(i)
    
Q.close()

Q = open(link + 'new.txt', 'w')
Q.write('hello world')
Q.close()

with open('new.txt', 'w') as f:
    f.write('hello world!')