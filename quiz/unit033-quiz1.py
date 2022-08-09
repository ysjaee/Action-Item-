# 호출 횟수를 세는 함수 만들기
# 함수 c를 호출할 때 마다 호출 횟수가 출력되게 만들기
def counter():
    i = 0
    def count():
        nonlocal i
        i +=1
        return i
    return count
c = counter()
for i in range(10):
    print(c(), end =' ')