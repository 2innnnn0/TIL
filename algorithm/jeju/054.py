# 054.py 
# 숫자가 순서대로 되어있진 않더라도, 연속수이면 YES 아니면 NO로 판별하는 프로그램 만들기.

# INPUT
# 1 2 4 3 5
# OUTPUT
# YES 

# INPUT
# 1 4 2 6 3 
# OUTPUT
# NO

user_input = input()
user_input = list(map(int, user_input.split(' ')))

def sol(l):
    l = sorted(l)
    for i in range(len(l)-1):
        if l[i]+1 != l[i+1]:
            return 'NO'
    return 'YES'

print(sol(user_input))



