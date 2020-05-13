# 046.py

# 문제 : 1~20까지의 모든 숫자를 일렬로 놓고, 모든 자릿수의 총합을 구하시오
# ex. 10~15 까지 모든 숫자를 일렬로 놓으면 , 101112131415 이고, 각 자리의 숫자를 더하면 25.

# range를 지정 min,max해서 구한다면.
min = int(input())
max = int(input())

result = 0
for i in list(range(min, max+1)):
    for j in str(i): 
        print(j)        
        result += int(j)
print(result)


# ---- solution 
s = 0
for i in list(range(21)):
    for j in str(i):
        result += int(j)
print(s)



