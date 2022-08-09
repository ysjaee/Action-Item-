#시간 이터레이터 만들기
# 표준 입력으로 정수 세 개 입력
# 시간 값은 문자열 시:분:초 형식 숫자 한자리일경우 앞에 0붙이기
# 시간은 반복을 끝낼 초 직전까지만 출력
class TimeIterator:
  def __init__(self, start, stop):
    self.start = start
    self.stop = stop

  def __getitem__(self, index):
    hour = (self.start + index) // 60 // 60 % 24
    minute = (self.start + index) // 60 % 60
    second = (self.start + index) % 60
    if index < self.stop - self.start:
      return '{0:02d}:{1:02d}:{2:02d}'.format(hour, minute, second)
    else:
      raise IndexError

start, stop, index = map(int,input().split())

for i in TimeIterator(start,stop):
    print(i)

print('\n', TimeIterator(start,stop)[index],sep='')