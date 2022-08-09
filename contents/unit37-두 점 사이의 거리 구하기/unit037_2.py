import math

# 클래스로 점 구현하기

class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = Point2D(x = 30, y = 20)
p2 = Point2D(x = 60, y = 50)

a = p2.x - p1.x
b = p2.y - p1.y

c = math.sqrt((a * a) + (b * b))
print(c)