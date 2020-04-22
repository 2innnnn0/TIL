# 27번
Tom Neal
70 100

> {'Tom':70, 'Neal':100}

key = input().split(' ')
value = map(int, input().split(' '))

value
print(key, list(value))
result = dict(zip(key, value))
print(result)


#+) map 정리
def f(n):
    return n ** 2
print(list(map(f, [2,3,4])))

a = [1,2,3,4]
b = [100,200,300,400]
c = ['a','b','c','d']
print(list(zip(a,b,c)))


print(dict(zip(c,a)))

print(dict(zip(c,[a,b])))
