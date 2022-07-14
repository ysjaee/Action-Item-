# while문 사용 이중리스트 출력
a = [[10,20],[30,40],[50,60]]

i = 0
while i < len(a):
    x,y = a[i]
    print(x,y)
    i+=1

# while문 두번 사용

i = 0
while i < len(a):
    j = 0
    while j <len(a[i]):
        print(a[i][j],end=' ')
        j+=1
    print()
    i +=1