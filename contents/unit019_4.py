# 계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end="")
    print()

# 별 감소시키기
for i in range(5):
    for j in range(5,0,-1):
        if i < j:
            print("*",end="")
    print()