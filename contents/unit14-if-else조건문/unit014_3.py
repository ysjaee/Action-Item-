# 조건식 여러개 지정
x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')

if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')