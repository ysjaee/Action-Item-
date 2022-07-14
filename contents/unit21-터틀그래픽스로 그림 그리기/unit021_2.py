# 터틀 그래픽으로 오각형 그리기
import turtle as t
t.shape('turtle')
for i in range(5):
    t.forward(100)
    t.right(360/5)

# 터틀 그래픽으로 육각형 만들기
for i in range(6):
    t.forward(100)
    t.right(360/6)