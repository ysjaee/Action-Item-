# 파일의 내용을 한 줄씩 읽기
with open('y.txt','r',encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))