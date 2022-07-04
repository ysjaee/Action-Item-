# 역삼각형 모양으로 별 출력시키기
for i in range(5):
    for j in range(5):
        if i<=j:
            print("*",end="")
        else:
            print(' ', end="")
    print()
