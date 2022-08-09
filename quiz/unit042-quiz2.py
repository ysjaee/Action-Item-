#HTML 태그 데코레이터 만들기
#표준 입력으로 HTML 태크 이름 두개 입력
#함수의 반환값을 HTML태그로 감싸는 데코레이터 만들기
# HTML 태그는 웹 페이지에 사용하는 문법
#<태그이름>으로 시작 </태그 이름>으로 끝

class html_tag:
  def __init__(self, tag_name):
    self.tag_name = tag_name

  def __call__(self, func):
    def wrapper():
      return '<{0}>{1}</{0}>'.format(self.tag_name, func())
    return wrapper
a, b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())