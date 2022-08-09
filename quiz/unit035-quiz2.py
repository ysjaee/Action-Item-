# 시간 클래스 만들기
# 표준 입력으로 시:분:초 형식의 시간이 입력
# Time 클래스를 완성하여 시,분,초가 출력되게 만들기
# from_stirng은 문자열로 인스턴스 만드는 메서드
#  is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드
# 시간은 24시까지 분은 59분, 초는 60초까지
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour < 25 and minute < 60 and second <61

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')