리스트 = [1, 2, 3, 4]

리스트.append(5)

print(리스트)

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
    if (i + 1) % 2 == 1:
        i += 1
        continue

    print(i + 1)    
    i += 1