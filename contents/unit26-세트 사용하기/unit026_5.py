# 집합 연산 후 할당 연산자 사용(세트에 추가하기)
a = {1,2,3,4}
a.update({5})
print(a)

# 세트에서 빼기
a = {1,2,3,4}
a.difference_update({3})
print(a)

# 세트에서 교집합 제외하고 가져오기
a = {1,2,3,4}
a.symmetric_difference_update({3,4,5,6})
print(a)