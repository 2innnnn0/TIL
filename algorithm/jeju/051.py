# 051.py
# 병합정렬 merg_sort 는 대표적인 정렬 알고리즘

# 1. 리스트의 길이가 0,1 이면 이미 정렬된 것으로 본다.
# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다
# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.


# 아래는 병합정렬 과정.
# 1. [1,3,5,4,8,6,7,2]
# 2. [1,3,5,4],[8,6,7,2]
# 3. [1,3][5,4][8,6][7,2]
# 4. [1][3][5][4][8][6][7][2]
# 5. [1,3][4,5][6,8][2,7]
# 6. [1,3,4,5],[2,6,7,8]
# 7. [1,2,3,4,5,6,7,8]

# def merge_sort():

# 강의에서는 쉬운 설명을 위해 한글로 입력, 실제 코테에세 하게되면 영어로@
def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while 그룹_하나 and 그룹_둘: # 둘중에 하나라도 있다면
        if 그룹_하나[0] < 그룹_둘[0]:
            결과값.append(그룹_하나.pop(0)) # 순서를 비교하고, 작은값이면 그룹에서 원소 빼기
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값

print(병합정렬([1,3,5,4,8,6,7,2]))