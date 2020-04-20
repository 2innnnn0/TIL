# 011.py

# 11번
# 1부터 100까지 모두 더하는 코드를 pass부분에 완성. (for 사용하기)

s = 0
pass
# 1+2+3+4+5+6


list_100 = []
for i in range(101):
    list_100.append(i)
sum(list_100)


range(10)
list(range(10))
type(range(10))




for i in range(101):
    s+=i
print(s)



class Knight:
    def __init__(self,health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

    def __str__(self):
        return 'hello world'