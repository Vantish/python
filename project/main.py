class Order:
    def __init__(self, username, product,quantity, price):
        self.username = username
        self.product = product
        self.quantity = quantity
        self.price = price
        self.ordercount = 0
    
    def createdict(self):
        tempdict = {'order_no' : self.ordercount,
                    'customer' : self.username,
                    'product' : self.product,
                    'quantity' : self.quantity,
                    'price' : self.price}
        return tempdict

def num1(lis):
    if type(lis) != list:
        print('리스트를 넣어주세요')
    else:
        username = input('고객명 :')
        product = input('제품명 :')
        quantity = input('제품 수량 :')
        price = input('제품 가격 :')
        temp = Order(username, product, quantity, price)
        temp.ordercount = generate_order_no()
        tempdic = temp.createdict()
        lis.append(tempdic)
        print(f'총 금액 : {int(temp.quantity) * int(temp.price)}')
        print('주문이 완료되었습니다.')

def num3(lis):
    if type(lis) != list:
        print('리스트를 넣어주세요')
    else:
        username = input('찾고싶은 고객명은 적어주세요 :')
        tempquantity = 0
        tempprice = 0
        tempname = ' '
        for i in lis:
            for a, t in i.items():
                if t == username:
                    tempname = username
                    tempquantity += int(i['quantity'])
                    tempprice += int(i['price']) * int(i['quantity'])
        print(f"고객명 : {tempname}\n",
            f"주문 수량 : {tempquantity}\n",
            f"주문 총액 : {tempprice}")

def num2(lis):
    if type(lis) != list:
        print('리스트를 넣어주세요')
    else:
         for i in lis:
                print(f"주문 번호 : {i['order_no']} ",
                      f"고객명 : {i['customer']} ",
                      f"제품명 : {i['product']} ",
                      f"수량 : {i['quantity']} ",
                      f"단가 : {i['price']} ",
                      f"총액 : {int(i['price']) * int(i['quantity'])}")

orderlis = []

def generate_order_no():
    if len(orderlis) == 0:
        return 1
    else:
        return len(orderlis) + 1

while True:
    print("1. 상품 주문하기")
    print("2. 전체 주문 이력 보기")
    print("3. 고객별 주문 통계")
    print("4. 끝내기")
    option = input("옵션을 선택하세요 :")

    if option == '4':
        realend = input("정말 종료하시나요? Y / N")
        if realend == 'Y':
            print("프로그램을 종료합니다.")
            break
        elif realend == 'N':
            print('초기 화면으로 돌아갑니다.')
        else:
            print("입력이 부정확합니다.")
    else:
        if option == '1':
            num1(orderlis)

        elif option == '2':
           num2(orderlis)

        elif option == '3':
            num3(orderlis)