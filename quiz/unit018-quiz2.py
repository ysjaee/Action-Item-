# 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준 입력으로 정수 2개가 입력
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작음
# 첫 번째 수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는 숫자가 출력되게 만들기
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=" ")
    i += 1