# 입력한 횟수대로 반복
count = int(input('반복할 횟수를 입력하세요: '))

for i in range(count):
    print('Hello, world!', i)

# 튜플의 요소로 반복
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in reversed ('python'):
    print(letter, end = ' ')