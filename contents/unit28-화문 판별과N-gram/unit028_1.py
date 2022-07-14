# 반복문으로 문자 검사하기
# 맞으면 true 틀리면 false
word = input("단어를 입력하세요: ")

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        is_palindrome = False
        break
print(is_palindrome)
