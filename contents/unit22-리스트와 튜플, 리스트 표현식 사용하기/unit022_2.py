# 리스트로 큐 구현
from collections import deque
a = deque([1,2,3])
print(a)
a.append(500) # 오른쪽에 요소 추가
print(a)
a.popleft() # 왼쪽에서 요소 삭제
print(a)