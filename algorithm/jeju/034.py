# 034.py

# 34번
[i.upper() for i in ['hello', 'world']]

user_input = input()
l = list(user_input.split(' '))
l
l = [int(i) for i in l]
l

# 역순
# sorted(l, reverse=True)

if l != sorted(l):
    print('NO')
else:
    print('YES')
