# 집합 연산
# 합집합
a = {1,2,3,4}
b = {3,4,5,6}
print(set.union(a,b))

# 교집합
print(set.intersection(a,b))

# 차집합
print(set.difference(a,b))
# 대칭차집합
print(set.symmetric_difference(a,b))