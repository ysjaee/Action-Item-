# 딕셔너리 표현식 사용하기
keys = ['a','b','c','d']
x = {key:value for key, value in dict.fromkeys(keys).items()}
print(x)