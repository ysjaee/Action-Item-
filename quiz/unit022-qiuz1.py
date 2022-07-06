#리스트 a에 들어있는 문자열 중에서 길이가 5인 것들만 리스트 형태로 출력되게 만들기

a = [ 'alpha','bravo','delta','echo','foxtrot','golf','hotel','india']
b = [i for i in a if len(i)==5]
print(b)