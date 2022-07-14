# 함수의 호출과정 알아보기
def mul(a,b):
    c = a * b
    return c

def add(a,b):
    c = a + b
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add(x,y)