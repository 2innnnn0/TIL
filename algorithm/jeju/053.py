# 053.py

user_input = input()

def 괄호체크(s):
    if s.count('(') != s.count(')'):
        return 'NO'
     = []
    for i in s :
        if i == '(':
            .append('(')
        if i == ')':
            if len() == 0:
                return 'NO'
            .pop()
    return 'YES'
    