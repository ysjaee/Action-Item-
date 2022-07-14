# lambda에 if 조건식 1 else 조건식 2 ese 식 3
a = [1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: str(x) if x == 1 else float(x) if x ==2 else x + 10, a)))