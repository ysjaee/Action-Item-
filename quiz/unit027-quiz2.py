# 특정 문자가 들어있는 단어 찾기
# 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램 만들기
# 콤마, 점 등은 출력 X (text 문장은 한 줄로 되어 있음)

with open('words2.txt', 'r') as file:
    words = file.readline()
    words = words.split()
    for word in words:
        if 'c' in word:
            print(word.strip(',.'))