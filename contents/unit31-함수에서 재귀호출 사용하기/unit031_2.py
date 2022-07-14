#종료조건이 있는 경우
def hello(count):
    if count == 0:
        return
    print('hello, world!', count)

    count -=1
    hello (count)
hello(5)