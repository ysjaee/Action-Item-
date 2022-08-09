# 사칙 연산 함수 만들기
x, y = map(int,input().split())
def calc(num1,num2):
    a = num1 + num2
    s = num1 - num2
    m = num1 * num2
    d = num1 / num2
    return a,s,m,d


a, s, m, d = calc(x,y)
print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a,s,m,d))