# 파일을 한 줄 씩 읽은뒤 \n없이 출력
# yield 사용
# 파일에는 compatibility,experience,photography,spotlight가 한 줄씩 써있음.
def file_read():
    with open('words.txt') as file:
        while True:
            line = file.readline()
            if line =='':
                break
            yield line.strip('\n')

for i in file_read():
    print(i)