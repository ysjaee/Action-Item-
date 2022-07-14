# reduce 사용하기
# from functools import reduce fuctools 모듈에서 reduce 함수 가져오기
# reduce(함수, 반복가능한 객체)
def f(x,y):
    return x + y

a = [1,2,3,4,5]
from functools import reduce
print(reduce(f,a))
