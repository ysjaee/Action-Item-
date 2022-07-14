# 딕셔너리로 키-값 쌍을 모두 출력
x = {'a':10,'b':20,'c':30,'d':40}
for key, value in x.items():
    print(key,value)

# 딕셔너리의 키만 출력
x={'a':10,'b':20,'c':30,'d':40}
for key in x.keys():
    print(key,end=' ')