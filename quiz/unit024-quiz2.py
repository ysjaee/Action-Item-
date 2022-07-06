# 표준 입력으로 문자열이 입력
# 입력된 문자열에서 'the'의 개수 출력
# 모든 문자가 소문자인 the만 찾아야되고 'them'등은 포함 x
x =input().split()
print(x.count('the'))