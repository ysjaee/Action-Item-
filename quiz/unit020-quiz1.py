# 1과 100사이의 숫자 중
# 2의 배수이거나 11의 배수이면 Buzz
# 2와 11의 공배수이면 FizzBuzz출력
for i in range(1,101):
    if i % 2 ==0 and i % 11 ==0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Buzz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)