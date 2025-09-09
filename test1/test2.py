tempstr = 'hi, nice to meet you'

print(tempstr.upper()) # HI, NICE TO MEET YOU
print(tempstr.lower()) # hi, nice to meet you

print(tempstr.title()) # Hi, Nice To Meet You

print(tempstr.split(',')) # ['hi', ' nice to meet you']


strings = 'ABCDEFG'

print(strings[3]) # D
print(strings[-2]) # F

print(strings[ : 3]) # ABC
# 인덱스 3의 문자열까지 출력되었다.
print(strings[2 : ]) # CDEFG
# 인덱스 2의 문자열부터 출력되었다.
print(strings[1 : 3]) # BC
# 인덱스 1번부터 (3 - 1)번 까지만 출력되었다.
print(strings[::-1]) # GFEDCBA

print(strings.replace('BCD', 'EFG')) # AEFGEFG
# 원래라면 ABCDEFG 가 출력되야 하지만, BCD가 EFG로 바뀌어서
# EFG가 두번 출력되었다.

strings = 'ABCDEDCBA'
print(len(strings)) # 9
print(strings.find('B')) # 1
# find 에서는 앞쪽에 있는 B를 먼저 찾았지만
print(strings.rfind('B')) # 7
# rfind 에서는 뒤쪽에 있는 B를 먼저 찾았다.


strings = 'AAABBCCCCDDD'
print(strings.count('A')) # 3
print(strings.count('C')) # 4

print('A' in strings) # True
print('E' in strings) # False

strings = ' 안녕하세요? 좋은 아침이에요! '
print(repr(strings.strip())) # '안녕하세요? 좋은 아침이에요!'
print(repr(strings.rstrip())) # ' 안녕하세요? 좋은 아침이에요!'
print(repr(strings.lstrip())) # '안녕하세요? 좋은 아침이에요! '
