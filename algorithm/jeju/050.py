# 050.py


# 버블 정렬은 두 인접한 원소를 검사하여 정렬하는 방법. 
# 시간복잡도는 느리지만, 코드가 단순하기 때문에 자주 사용


def bubble(n, data):
    for i in range(n-1):  # 한번 순회가 끝나면, 마지막 자리는 가장 큰 값.
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  # swap
    for i in range(n):
        print(data[i], end=" ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)