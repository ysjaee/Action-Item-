# x를 y로 나누었을 때 몫과 나머지가 출력되게 만드세요
x = 10
y = 3

def get_quotient_remainder(a, b):
    return a // b, a % b

quotient, remainder = get_quotient_remainder(x,y)
print('몫:{0}, 나머지:{1}'.format(quotient,remainder))