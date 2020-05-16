# 조건이 있는 list comprehensions
# %는 나누고 남은 나머지. 즉, num%2==0은 2로 나눈 나머지가 0이라는 의미이므로 2의 배수.
result = [num ** 2 for num in range(10) if num%2 == 0]
print(result)


# 위와 다르게, 짝수가 아닌경우에는 0을 반환하기로 했다. 
result2 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(result2)

# dict Comprehension 
# [] 대신 {}을 사용한다.
# 그리고 출력표현식을 콜론(:) 으로 구분한다.
pos_neg = {num: -num for num in range(9)}
print(pos_neg)
print(type(pos_neg))