# 변수 x가 11과 20 사이면 '11~20' 출력
# 변수 x가 21과 30 사이면 '21~30' 출력
# 아무것도 해장하지 않으면 '아무것도 해당하지 않음' 출력
x = int(input())

if x>= 11 and x<= 20:
    print('11~20')
elif x>20 and x<31:
    print('21~30')
else:
    print('아무것도 해당하지 않음')