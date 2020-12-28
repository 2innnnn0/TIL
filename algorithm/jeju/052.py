# 052.py 퀵정렬 만들기

# 퀵정렬. 기준값을 기준으로 하나씩 정렬하는 방법.

def quick_sort(input_list):
    input_list_len = len(input_list)
    # 입력된 값이, 단일값이면 그대로 돌려줌.
    if input_list_len <= 1:
        return input_list

    value = input_list.pop(input_list_len//2)
    group_1 = []
    group_2 = []
    # 0번째 인덱스값부터 기준값을 비교.
    # 기준값이 더 크다면 group1에 넣기. 작다면 group2에 넣기. 
    for i in range(0, input_list_len-1):
        if input_list[i] < value:
            group_1.append(input_list[i])
        else:
            group_2.append(input_list[i])
    return quick_sort(group_1) + [value] + quick_sort(group_2)

input_list = input().split(' ')
input_list = [int(i) for i in input_list]
print(input_list)
print(quick_sort(input_list))

# ------ 퀵정렬.
# [1,3,2,7,5,6,4,8,9,10] -> 길이가 10. 그 절반인 5가 기준값이므로 6이 기준값.
# [1,3,2,5,4] ,6, [7,8,9,10] 
# [1], 2, [3,5,4] 6, [7,8] 9 [10] -> 2와 9가 기준값
# 1, 2 [3,4], 5 6, [7] 8 9 10 -> 5와 8이 기준값
# 1, 2 [3] 4, 5 6, 7 8 9 10 -> 4가 기준
# 1, 2 3 4, 5 6, 7 8 9 10 