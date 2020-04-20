# 018.py
# 18번
20 30 40
> 30

n = input()
n
l = n.split(' ')
print(l)
changel = []

for i in l :
    changel.append(int(i))


print(sum(changel)//3)