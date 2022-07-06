# for 반복문으로 2차원 리스트 만들기
a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a)
