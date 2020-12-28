# 053.py 괄호가 올바르게 닫혀있으면 YES, 아닌경우 NO.

user_input = input()
# e.g. ((()))(()))(

# -- YES 
# 1. (())
# 2. ((()()())())
# 3. ()()()
# -- NO 
# 4. )))((( 
# 5. ())
# 6. ()(

def 괄호체크(s):
    # 열림과 닫힘의 갯수가 동일해야함.
    if s.count('(') != s.count(')'):
        return 'NO'
    괄호 = []
    for i in s :
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:
                return 'NO'
            괄호.pop()
    return 'YES'
    
print(괄호체크(user_input))