# 063.py
# 앞글자만 따서 출력하기
# 복잡한 세상 편하게 살자 -> 복세편살

user_input_list = input().split(' ')
# 1. 띄어쓰기로 구분된 리스트 
# input_list = ['복잡한','세상','편하게', '살자']

result = ''
# 2. 리스트의 각 요소별 0번쨰값을 불러오기.
for s in user_input_list:
    result += s[0]
    # print(i[0], end='')

print(result)
