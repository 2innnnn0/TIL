# 029.py
# 29번
# dir()

type('a')
'a'.isupper()
'A'.isupper()

def tf(input):
    if input.isupper():
        print('YES')
    else:
        print('NO')
tf('A')
tf('b')

tf('1')

dir('a')


+) SOLUTION : ASCII를 이용하심
문자를 아스키코드로 변환하는 함수 ord()
print(ord('a'))

user_input=input()
if ord(user_input) >= 65 and ord(user_input) <= 90:
    print('YES')
else:
    print('NO')