# 040.py
# 40번
# 제한무게.
total = 0
count = 0

limit = int(input()) #무게제한
n = int(input()) #탑승수

for i in range(n):
    if total <= limit:
        total += int(input())
        count = i
print(i)

