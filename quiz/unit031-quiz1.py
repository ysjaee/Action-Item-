# 재귀호출로 회문 판별하기
# 문자열이 회몬운지 판별하고 결과를 True, False로 출력되게 만들기
def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('hello'))
print(is_palindrome('level'))
