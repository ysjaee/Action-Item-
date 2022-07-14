# 문자열 분리하여 리스트 만들기
a ='apple pear grape pineapple orange'.split()
print(a)
# 구분자 문자열과 문자열 리스트 만들기
b = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(b)

# 문자열 왼쪽,오른쪽 가운데 정렬
print('python'.rjust(10))
print('python'.ljust(10))
print('--python--'.center(11))
