# 산 모양으로 별 만들기
# 표준 입력으로 산 높이 결정
x = int(input("산 높이 입력:"))

for i in range(x):
    for k in range(x,i+1,-1):
        print(' ',end='')

    for k in range((i*2)+1):
        print("*",end='')
    print()