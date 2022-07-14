# 파일의 내용을 한 줄 씩 가져오기
with open('y.txt','r',encoding='utf-8') as file:
    lines =file.readlines()
    print(lines)