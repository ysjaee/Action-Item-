# 언패킹 사용하기
# 인수를 순서대로 넣을 때는 리스트나 튜플을 사용

def print_numbers(a,b,c):
    print(a)
    print(b)
    print(c)
x = [10,20,30]
print_numbers(*x)