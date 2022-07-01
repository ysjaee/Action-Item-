# 온라인 할인 쿠폰 시스템 만들기
# 표준입력으로 가격과 쿠폰 이름이 각 줄에 입력
# cash 3000원 쿠폰은 3000원, cash5000 쿠폰은 5000원 할인
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램 만들기
total = 0
a = input("가격 입력:")
b = input("Cash3000 or Cash5000입력:")
Cash3000 = 3000
Cash5000 = 5000

if b == 'Cash3000':
    print(int(a)-3000)
elif b == 'Cash5000':
    print(int(a)-5000)