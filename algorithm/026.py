# 026.py

# 26번
def solar(kor):
    l_kor = ['수성', '금성', '지구' ,'화성','목성','토성','천왕성','해왕성']
    l_eng = ['1', '2', '3' ,'4','5','6','7','8']

    l_dict=dict(zip(l_kor, l_eng))

    return l_dict[kor]

solar('금성')