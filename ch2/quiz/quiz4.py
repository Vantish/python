lis = [100, 77, -5, 10]

int = 0

while int < len(lis):
    if lis[int] < 0:
        int += 1
        continue
    
    print(lis[int])
    int += 1


# 반복문으로 요소를 하나씩 출력하다가 77을 만나면 break를 사용해 반복문을 종료하세요

qnt = 0
while qnt < len(lis):
    if lis[qnt] == 77:
        break

    print(lis[qnt])
    qnt += 1


