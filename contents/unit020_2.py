# 코드 단축하기
for i in range(1, 101):
    print("Fizz"*(i % 3 ==0) + "Buzz" * (i % 5 ==0) or i)