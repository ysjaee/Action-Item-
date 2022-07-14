#자동으로 파일 객체 닫기
with open('x.txt','r') as file:
    s = file.read()
    print(s)