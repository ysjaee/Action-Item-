# 슬라이스 사용
a=range(10)[slice(4,7,2)]
print(a)
b=range(10).__getitem__(slice(4,7,2))
print(b)