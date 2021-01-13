# 064.py

# 정량 N에 정확히 맞춰야만 움직이는 화물용 엘베.
# 7kg, 3kg 두가지 화물. 
# e.g. 24kg정량이라면, 3kg을 8개 옮기기 보다, 7kg 3개. 3kg 1개. 총 4개로 적게 옮기고 싶음.

# 입력 N.
# 가장 적게 옮길 수 있는 횟수를 출력하기. 어떻게 해도 정량이 N이 되지 않는다면 -1을 출력하기.



# 1. 7로 나누기로 한뒤 몫을 제외한 나머지를 3으로 나누기. 이떄 나머지는 0 이어야함.

# N=24
# 24/7 = 몫:3, 나머지:3 -> 3/3 = 몫:1, 나머지:0

# print(24/7)
# print(24//7)
# print(24%7)

N = int(input())
result = 0

if (N%7)%3==0:
    result += (N//7)
    if (N%7)==0:
        pass
    else:
        result += (N//7)//3
else:
    result = -1
print(result)


# SOL
while True:
    if N % 7 == 0:
        result += N//7 
        print(result)
        break
    N -= 3
    result +=1
    if N < 0 :
        print(-1)
        break

