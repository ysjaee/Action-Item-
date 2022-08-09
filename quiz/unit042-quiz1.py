#연습 문제: 데코레이터로 매개변수의 자료형 검사하기
# 데코레이터 type_check를 입력
# 지정된 자료형이면 정상적으로 호출, 지정한 자료형과 다르면 Runtimeerror 예외를 발생시키면서 '자료형이 다릅니다.'에러 메세지를 출력

def type_check(type_a,type_b):
    def real_decorator(func):
        def wrapper(a,b):
            if isinstance(a, type_a) and isinstance(b,type_b):
                return func(a,b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator

@type_check(int,int)
def add(a,b):
    return a + b

print(add(10,20))
print(add('hello','world'))