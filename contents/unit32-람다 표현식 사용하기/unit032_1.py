# 람다 표현식을 인수로 사용하기
def plus_ten(x):
    return x + 10

print(list(map(plus_ten,[1,2,3])))

print(list(map(lambda x: x + 10, [1,2,3])))