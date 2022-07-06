# sorted로 2차원 리스트 정렬하기
students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]

print(sorted(students, key = lambda student: student[1]))
print(sorted(students, key = lambda student: student[2]))

