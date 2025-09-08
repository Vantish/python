# 문자열 관련 함수

# replace : 문자열 교체 함수
# 문자열 자체가 가진 함수로 첫번째 인자에는 바꿀 단어, 두번째 인자에는 바뀔 단어,
# 세번째 인자로는 몇번 반복할지 숫자가 들어간다(= 0)
print("banana".replace('anan', 'babb', 2))
print("010-1234-5678".replace('-', ':'))
print("010-1234-5678".replace('-', ''))

# repr : 따옴표를 표시하는 함수
print("hello")
print(repr("hello"))

# 공백 제거 함수
print(repr(" hello world ".strip()))
print(repr(" hello world ".rstrip()))
print(repr(" hello world ".lstrip()))

# 첫글지만 대문자로 바꾸는 함수
print("hello world".title())