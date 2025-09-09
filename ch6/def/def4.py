# def add(a, b):
#     return a + b

add = lambda a, b: a + b

strings = ['foo', 'card', 'ba', 'aaa']

strings.sort(key = lambda s : len(s))

print(strings)