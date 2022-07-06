# 문자열 바꾸기
print('Hello, world!'.replace('world','python'))

# 문자 바꾸기

table = str.maketrans('abcde','12345')
print('apple'.translate(table))