# 041.py

# 41번
# 소수 여부
del(int)
integer = int(input())

ch= True

for i in range(2,integer):
    if integer % i == 0:
        ch = False
if ch == True:
    print('yes')
else:
    print('no')
