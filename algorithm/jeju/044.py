# 044.py

# 문제 : 사용자가 입력한 양이 정수의 각 자리수의 합을 구하는 프로그램을 만들기.
# ex. 18234 = 1+8+2+3+4 -> return 18

user_input = input()

# input값을 인덱스로 모두 해체하기.
# 빈 리스트 생성, append한 후 sum
a = []
for i in range(len(user_input)):
    # print(user_input[i])
    a.append(int(user_input[i]))
sum(a)


# ------ 답안 
n = input()
result = 0
for i in n :
    result +=int(i)
print(result)