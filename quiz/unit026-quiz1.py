# 공배수 구하기
# 1부터 100까지 3과 5의 공배수를 세트 형태로 출력되게 만들기

a = {i for i in range(1,101) if i % 3 == 0}
b = {i for i in range(1,101) if i % 5 == 0}

print(a & b)