class Calc:
    calctype = '기본 계산기'

    def __init__(self, color):
        self.calc_color = color

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
class NewCalc(Calc):
    calctype = '공학용 계산기'

    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

temp = Calc('red')

print(type(temp))

print(temp.add(3,4))

temp1 = NewCalc('green')
print(temp1.calctype)
print(temp1.mul(3, 5))
