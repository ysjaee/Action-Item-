# 키워드 인수와 딕셔너리 언패킹 사용하기
def personal_info(name,age,address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
