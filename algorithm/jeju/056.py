# 056.py
# 주어진 딕셔너리에서 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하기.
nationWidth = {
    'korea' : 220877,
    'rusia' : 17098242,
    'china' : 9596961,
    'france' : 543965,
    'japan' : 377915,
    'england' : 242900,
}

# print(nationWidth['korea'])
# 순회하면서 korea와의 차이가 가장 작은 절대값을 출력하면 됨.

koreaWidth = nationWidth['korea']
nationWidth.pop('korea')
l = list(nationWidth.items())

print(l)
gap = max(nationWidth.values())
for i in l:
    print(abs(koreaWidth - i[1]))
    
    # 순회하면서, 기존에 저장된 값보다 작으면 그 값을 입력, 아니면 패스.
    if gap > abs(koreaWidth - i[1]):
        gap = abs(koreaWidth - i[1]) 
        item = i

print(item[0], gap)
    