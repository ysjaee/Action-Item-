# 재귀호출로 피보나치 수 구하기
# 표준 입력으로 정수 한 개 입력(10~30)
# 피보나치 수는 0과1로 시작, 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-2)+fib(num-1)

n = int(input())
print(fib(n))