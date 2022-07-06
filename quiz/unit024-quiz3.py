# 높은 가격순으로 출력
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력
# 각 가격은 ;으로 구분
# 가격을 높은 가격순으로 출력하는 프로그램 만들기
# 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬, 천 단위로 ,찍기

a=list(map(int, input().split(';')))
a.sort(reverse=True)
for x in a:
  print('{:>9,}'.format(x))