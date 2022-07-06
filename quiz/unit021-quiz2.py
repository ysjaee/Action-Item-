# 꼭짓점 개수와 선 길이가 입력
# 별이 그려지게 만들기 (시계 방향으로 그려지게)
import turtle as t
t.shape('turtle')

a = int(input())
b = int(input())

if a >= 5 and a <= 10:
    if b >= 50 and b <= 150:
        for i in range(a):
            t.forward(b)
            t.right((360/a)*2)
            t.forward(b)
            t.right(360-(360/a))

