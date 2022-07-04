# 교통카드 시스템
# 표준 입력으로 나이가 입력. 교통카드 시스템에서 시내버스 요금은 다음과 같으며 각 나이에 맞게 요금을 차감한 뒤 잔액이 출력되게 만들기
# 현재 교통카드에는 9000원
# 어린이(만 7세 이상 12세 이하) 650원
# 청소년(중,고등학생 만 13세 이상 18세 이하) 1050원
# 어른 (만 19세 이상) 1250원

age = int(input())
balance = 9000
if age >= 7 and age <= 12:
    balance = balance - 650
elif age >= 13 and age <= 18:
    balance = balance - 1050
elif age >= 19:
    balance = balance - 1250
print(balance)