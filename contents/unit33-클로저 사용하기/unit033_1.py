# 현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하기 위해 nonlocal 키워드를 사용
def A():
    x = 10
    def B():
        nonlocal x
        x = 20

    B()
    print(x)

A()