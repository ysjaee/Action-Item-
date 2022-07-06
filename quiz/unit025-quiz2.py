# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두줄로 입력
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성
# 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값쌍을삭제 하도록 만들기
keys = input().split()
values = map(int,input().split())

x = dict(zip(keys, values))
x.pop('delta')
x = {key: value for key, value in x.items() if value != 30}

print(x)


#alpha bravo charlie delta
#10 20 30 40