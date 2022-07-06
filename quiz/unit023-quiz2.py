# 표준 입력으로 2차원 리스트의 가로 세로 입력
# 그다음 줄부터 리스트의 요소로 들어갈 문자가 입력
# 2차원 리스트 안에서 *는 지뢰 .은 지뢰 x
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램 만들기
# 여러 줄을 입력받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 append로 각줄을 추가하면 됨
col, row = map(int, input().split())
count = 0
matrix = []

for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            pass
        else:
            matrix[i][j] = 0
            for k in range(i - 1, i + 2):
                for x in range(j -1, j + 2):
                    if k < 0 or x < 0 or k >= row or x >= col:
                        pass
                    elif matrix[k][x] == '*':
                        matrix[i][j] += 1
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()