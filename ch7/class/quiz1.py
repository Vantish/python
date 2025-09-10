class Book:
    def __init__(self, title, author,price):
        self.book_title = title
        self.book_author = author
        self.book_price = price
    
    def info(self):
        print(f"책 이름 : {self.book_title}\n" 
              f"책 저자 : {self.book_author}\n"
              f"책 가격 : {self.book_price}")

쌀다팜 = Book('나는 쌀다팜', '쌀사자 보이즈', 6400000)
쌀다팜.info()

class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color

    def info(self):
        print(f"차종은 {self.car_name}\n"
              f"색상은 {self.car_color}") 
        
sonata = Car('소나타', '흰색')
sonata.info()

avante = Car('아반떼', '검정')
avante.info()

class Order:
    def __init__(self, id, name, quantity):
        self.order_id = id
        self.order_name = name
        self.order_quantity = quantity

    def idandname(self):
        print(f"주문번호는 {self.order_id} 입니다.\n"
              f"상품명은 {self.order_name} 입니다.")

test1 = Order(101, '노트북', 3)
test1.idandname()
test2 = Order(102, '마우스', 5)
test2.idandname()

class Coffee:
    def __init__(self, name, price):
        self.coffee_name = name
        self.coffee_price = price
        self.__coffee_order = 0
    
    def cfif(self):
        print(f"{self.coffee_name} {self.coffee_price}원")
        self.__coffee_order += 1
    
    def howmanyorder(self):
        return self.__coffee_order

    

ame = Coffee('아메리카노', 1600)
RaT = Coffee('라떼', '3000')
mura = Coffee('머라카노', 50000)
uma = Coffee('우마리카노', 300000)

ame.cfif()
ame.cfif()
ame.cfif()
ame.cfif()

RaT.cfif()
RaT.cfif()
RaT.cfif()

mura.cfif()
mura.cfif()

uma.cfif()
uma.cfif()
uma.cfif()
uma.cfif()
uma.cfif()
uma.cfif()

print(ame.howmanyorder(), RaT.howmanyorder(), mura.howmanyorder(), uma.howmanyorder())

class Bus:
    def __init__(self, number):
        self.bus_number = number
        self.__customer_count = 0
    
    def inside_to_bus(self, incoming):
        self.__customer_count += incoming
        print(f"{self.bus_number} 버스에 {incoming}명이 탑승했습니다.\n"
              f"현재까지 {self.bus_number}에 탑승한 손님은 총 {self.__customer_count}명 입니다.")
        
class Subway:
    def __init__(self, number, price = 1500):
        self.bus_number = number
        self.__customer_count = 0
        self.price = price
        self.__all_price = 0
        
    def howmuch(self):
        self.__all_price = self.price * self.__customer_count
        return self.__all_price
    
    def inside_to_Subway(self, incoming):
        self.__customer_count += incoming
        print(f"{self.bus_number}호선에 {incoming}명이 탑승했습니다.\n"
              f"현재까지 {self.bus_number}호선에 탑승한 손님은 총 {self.__customer_count}명 입니다.\n"
              f"총 요금은 {self.howmuch()}원 입니다.")


nine = Bus(9)
nine.inside_to_bus(3)
nine.inside_to_bus(6)
nine.inside_to_bus(1)

hund = Bus(111)
hund.inside_to_bus(20)
hund.inside_to_bus(5)
hund.inside_to_bus(3)

two = Subway(2)
two.inside_to_Subway(3)
two.inside_to_Subway(5)
two.inside_to_Subway(10)

sev = Subway(7, 3000)
sev.inside_to_Subway(10)
sev.inside_to_Subway(30)
sev.inside_to_Subway(27)

class Account:
    def __init__(self, money = 0):
        self.left_money = money

    def deposit(self, money):
        self.left_money += money
        print(f"{money}원 입금\n"
              f"현재 잔액은 {self.left_money}원 입니다")

    def withdraw(self,money):
        if self.left_money < money:
            print('출금 실패\n'
                  '잔액이 부족합니다')
        else:
            self.left_money -= money
            print(f"{money}원 출금"
                  f"현재 잔액은 {self.left_money} 입니다")
            
showmethemoney = Account(30000)
showmethemoney.deposit(40000)
showmethemoney.deposit(10000)
showmethemoney.withdraw(119000)

