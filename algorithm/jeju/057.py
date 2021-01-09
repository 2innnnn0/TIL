# 057.py
# 0부터 1000까지 1의 갯수를 세는 프로그램을 만들기  
# INPUT : 20 
# OUTPUT : 1 10 11 12 ... 19 -> 12개.

# 1. n을 1부터 n까지 나열하기. 10- > 1,2,3,4,5 ->
# print(list(range(1, n+1)))

# 2. 나열된 수를 문자열로 변환하기.
# print(list(map(str, list(range(1, n+1)))))

# 3. 문자열을 다시 쪼개기 -> 안해도 됨.
# print()

# 4. '1'을 카운트하기.
# list(map(str, list(range(1, n+1))))
# print(str(list(range(10))))

# SOL1
def count(n):
    countN = 0
    s = str(list(range(n+1)))
    print(s)
    for i in s:
        if i == '1':
            countN += 1 
    return countN
print(count(1000))

# SOL2
def count2(n):
    count = str(list(range(n+1))).count('1')
    return count

print(count2(1000))