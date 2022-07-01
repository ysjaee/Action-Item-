# 표준입력으로 국어, 영어, 수학, 과학 점수 입력
# 네 과목의 평균이 80점 이상일 때 합격
# '합격', '불합격'으로 출력
total = 0
average = 0
korean, english, math, science = input().split()
korean = int(korean)
english = int(english)
math = int(math)
science = int(science)
if korean <= 0 or korean >= 100 or english <= 0 or english >= 100 or math <= 0 or math >= 100 or science <= 0 or science >= 100:
    print("잘못된 점수 출력")
else:
    total = korean + english + math + science
    average = total/4
    print(average)