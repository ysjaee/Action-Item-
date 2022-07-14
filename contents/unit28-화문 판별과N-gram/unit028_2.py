# 리스트와 reversed 사용
word = 'level'
print(list(word) == list(reversed(word)))
# join 메서드와 reversed 사용
word = 'level'
print(word == ''.join(reversed(word)))
