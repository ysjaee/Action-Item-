# 날짜 클래스 만들기
# Date class 완성
# is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드
# 월은 12월 일은 31일까지

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int,date_string.split('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2000-10-31'):
    print('올바른 형식입니다.')
else:
    print("잘못된 날짜 형식입니다.")