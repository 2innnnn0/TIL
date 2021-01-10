# 061.py
# 문자열 압축 표현.
# aaabbbbcddddaa -> 3a4b1c4d2a로 압축하여 표현하기.
# ababab -> 3ab로 압축하기

# SOL
user_input = input()
s = ''
storeString = user_input[0]
count = 0 
for i in user_input: 
    if i == storeString: 
        count += 1 
    else :
        s += str(count) + storeString 
        storeString = i 
        count = 1 
s += str(count) + storeString 
print(s) 


# 정규표현식. SOL
import re as re
input_user = input()
rule = re.compile('[a-c]+')

one = re.findall('b', input_user)
two = re.findall(rule, input_user)
three = re.findall('(\\w)(\\1*)', input_user)

print(one)
print(two)
print(three)


s = ''
for i,j in three:
    s += str(len(j)+1) + i 
print(s)


# 정규표현식
# . ^ $ {} [] () \ | * 
# [a-zA-Z] 알파벳 모두 
# \d 숫자
# \s 문자 
# \w 문자와 숫자 매칭
# \W 문자와 숫자가 아닌 문자열들을 매칭 [%a-zA-Z0-9]
# *는 반복 +도 반복
# match, search, findall, finditer