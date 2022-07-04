# 첫 번째 입력 값의 범위 1~1000
# 두 번째 입력 값의 범위 10~1000
# 두 입력한 값 사이의 숫자 사이 중 5의 배수이면 Buzz, 7의 배수이여도 Buzz
# 5와 7의 공배수이면 FizzBuzz
# 두 번째 수가 첫 번째 수보다 커야됌

a = int(input())
b = int(input())
num = a
if num <= b:
    for i in range(a,b+1):
        if num % 5 == 0 and num % 7 ==0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 7 == 0:
            print("Buzz")
        else:
            print(num)
        num+=1