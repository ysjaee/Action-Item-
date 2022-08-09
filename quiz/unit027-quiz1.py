# 단어가 줄 단위로 저장된 words.txt 파일이 주어짐
# 10자 이하인 단어의 개수가 출력되게 만들기

with open('words.txt','r',encoding='utf-8') as file:
    words = file.readlines()
    count = 0
    for word in words:
        if len(word.rstrip('\n'))<=10:
            count +=1
    print(count)