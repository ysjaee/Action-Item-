# 표준 입력으로 양의 정수 두 개가 입력
# 두 숫자의 공약수를 세트 형태로 구하기
# 최종 결과는 공약수의 합
a,b=map(int,input().split())
a = {i for i in range(1,a+1) if a % i == 0}
b = {i for i in range(1,b+1) if b % i == 0}
divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)