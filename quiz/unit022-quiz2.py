#표준 입력으로 정수 2개 입력
# 첫번째 값 1~20 두번째 값 10~30
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭 제곤 리스트를 출력하는 프로그램 만들기
# 리스트 두 번째와 마지막에서 두 번째는 제외시키기

a = int(input())
b = int(input())
result = []
c = 1
if 1 <= a and a <= 20:
    if 10 <= b and 30>= b:
        for i in range(a,b+1):
            c = 2**i
            result.append(c)
    result.pop(1)
    result.pop(-2)
print(result)