# 파일에서 화문인 단어 출력하기
# 단어가 줄 단위로 저장된 words.txt 파일에서 화문인 단어를 각 줄에 출력하는 프로그램 만들기
# 단어 출력할 때 등장한 순서대로 출력
# \n제외한 뒤 화문인지 판단 단어 출력시에도 없어야 됨

with open('word1.txt','r') as file:
    text = None
    a = []
    while text != "":
        text = file.readline().strip('\n')
        a.append(text)
    for i in range(0,len(a)-1):
        temp = a[i]
        if list(temp) == list(reversed(temp)):
            print(temp)
