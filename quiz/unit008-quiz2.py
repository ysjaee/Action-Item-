# 표준 입력으로 국어, 영어, 수학, 과학 점수 입력
# 국어 90점이상, 영어 80점 초과, 수학 85점 초과, 과학 80점 이상일 때 합격
# 합격이면 True 불합격이면 False

korean,english,math,science = input().split()
korean = int(korean)
english = int(english)
math = int(math)
science = int(science)
print(korean >= 90 and english > 80 and math > 85 and science >= 80)
