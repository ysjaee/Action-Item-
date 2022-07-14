# 딕셔너리 응용
# setdefault: 키-값 쌍 추가
# update : 키의 값 수정

x = {'a':10,'b':20,'c':30, 'd':40}

x.setdefault('e')
print(x)
x.setdefault('f',100)
print(x)

# 값 수정
x.update(a=90)
print(x)