# 1과 100사이의 숫자 중
# 3의 배수이거나 5의 배수이면 Buzz
# 3과 5의 공배수이면 FizzBuzz출력
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Buzz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
