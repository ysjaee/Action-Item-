# 반복문으로 2차원 리스트의 요소 모두 출력
a = [[10,20],[30,40],[50,60]]
for x,y in a:
    print(x,y)

# for 반복문 2번 사용

for i in a:
    for j in i:
        print(j,end=' ')
    print()
