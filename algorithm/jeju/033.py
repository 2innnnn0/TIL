# 033.py
# 33번
number = input()
number_list = list(number.split(' '))
number_list = [int(i) for i in number_list]
number_list

# number_list[::-1]

for i in range(len(number_list)-1, -1, -1):
    print(number_list[i], end=' ')
