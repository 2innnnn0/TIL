# 049.py

# 순서가 없는 10개의 숫자가 공백으로 구분, 주어진 숫자들 중 최대값을 반환

# -- 하나씩 비교해가면서, sort해서 최대값을 고르는 문제.**
# 참고 https://wikidocs.net/16041

input_list = [4,1,2,10]
print(sorted(input_list)[-1])
# 또는
# revered, iterable한 객체를 반환, 확인을 위해서는 list로 한번 더 변형 필요
print(list(reversed(input_list))[0])



# --- solution 
data =  list(map(int, input().split()))
print(max(data))