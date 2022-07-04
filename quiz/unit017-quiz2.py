# 표준 입력으로 금액이 입력
# 1회당 요금은 1350원으로 교통카드를 사용할 때 마다 각 줄에 잔액을 출력
total = int(input())
result = total - 1350
while result >= 0:
    print(result)
    result -= 1350

