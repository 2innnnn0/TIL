# 043.py

# 문제 : 10진수를 2진수로 변환하기 
a = int(input())
b = []

while a:
    b.append(str(a % 2))
    a = int(a/2)
b.reverse()
print(int(''.join(b)))