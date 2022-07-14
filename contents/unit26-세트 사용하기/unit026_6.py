# 부분 집합과 상위집합 확인
# 부분집합인지 확인
a ={1,2,3,4}
print(a <= {1,2,3,4})
print(a.issubset({1,2,3,4,5}))

# 상위집합인지 확인
print(a>={1,2,3,4})
print(a.issuperset({1,2,3,4}))

# 같은지 다른지 확인
print(a == {4,1,2,3})
print(a != {1,2,3})

# 세트가 겹치지 않는지 확인
print(a.isdisjoint({5,6,7,8}))
print(a.isdisjoint({3,4,5,6}))