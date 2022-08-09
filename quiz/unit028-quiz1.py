# 단어 단위 N-gram만들기
# 표준 입력으로 정수와 문자열이 입력
# N-gram튜플로 출력(리스트 표현식 사용)
# 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'출력

n = int(input())
text = input()
words = text.split()
if len(words) < n:
    print("wrong")
else:
    n_gram = zip(*[words[i:] for i in range(n)])
    for i in n_gram:
        print(i)