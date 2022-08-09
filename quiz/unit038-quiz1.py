try:
    file = open('maria.txt','r',encoding = 'utf-8')
except FileNotFoundError:
    print('파일이 없습니다.')
else:
    s = file.read()
    file.close()