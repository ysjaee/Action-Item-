# 소수 제너레이터 만들기
# 정수 입력 두 개
# 첫 번째 입력 값의 범위 10~1000
# 두 번째 입력 값의 범위 100~1000
#첫 번째 정수부터 두 번째 정수 사이의 소수 생성
def prime_number_generator(start, stop):
    for n in range(start, stop):
        is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
        if is_prime:
            yield n
start, stop = map(int,input().split())

g = prime_number_generator(start,stop)
print(type(g))
for i in g:
    print(i, end = ' ')