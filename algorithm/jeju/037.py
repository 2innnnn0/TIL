# 037.py
# 37번
l = input().split()

l

count = 0
l


len(l)

for i in range(1, len(l)):
    if l.count(l[i-1]) < l.count(l[i]):
        count = i

print('{}(이)가 총 {}표로 반장이 되었습니다.'.format(l[count], l.count(l[count])))
