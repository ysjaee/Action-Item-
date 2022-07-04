# 별 대각선으로 출력시키기
for i in range(5):
    for j in range(5):
        if j == i:
            print("*",end="")
        else:
            print(' ', end="")
    print()