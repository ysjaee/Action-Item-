# 파일경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\python36-32\\python.exe'

x= path.split('\\')
filename =x[-1]
print(filename)