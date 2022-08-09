# 표준 입력으로 x,y 좌표 4개가 입력되어 point2D 클래스의 인스턴스 리스트에 저장
# 점 4개는 첫 번째 점에서 마지막 점까지 순서대로 이어져 있다.
# 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만들기

import math

class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int,input().split())
a = p[1].x - p[0].x
b = p[1].y - p[0].y

c = p[2].x - p[1].x
d = p[2].y - p[1].y
e = p[3].x - p[2].x
f = p[3].y - p[2].y
length = math.sqrt((a * a) + (b * b)) + math.sqrt((c * c) + (d * d)) + math.sqrt((e * f) + (e * f))



print(length)