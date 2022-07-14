# 반복문으로 N-gram 출력
text = 'hello'

for i in range(len(text)-1):
    print(text[i], text[i+1], sep='')

# 문장을 N-gram으로 출력
text = 'this is python script'
words = text.split()
for i in range(len(words)-1):
    print(words[i],words[i+1])