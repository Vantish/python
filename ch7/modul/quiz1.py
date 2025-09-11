import include


print(include.math.ceil(3.14))
print(include.math.floor(3.14))

for _ in range(1, 7):
    print(include.random.randint(1, 684513))

include.time.sleep(2)
print("끝!")
include.time.sleep(3)
print("3초 경과")
print(include.os.getcwd())