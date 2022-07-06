# 가장 작은 수
a = [38, 21, 53, 62, 19]

smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

print(smallest)
# 가장 큰 수
largest = a[0]

for i in a:
    if i > largest:
        largest = i

print(largest)