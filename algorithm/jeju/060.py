# 060.py
# 이름을 가나다 순서대로 배정하고 번호를 매기기.

student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']

# 정렬을 하는 두가지 방법 
print(student.sort()) # 1. 리스트에 직접 sort()
print(sorted(student)) # 2. sorted를 적용한 것을 변수에 다시 저장.

for n, name in enumerate(sorted(student),1): # 두번째 파라미터에 1부터 시작을 하는 옵션 넣기
    print('번호:{}, 이름: {}'.format(n,name))

# for n, name in enumerate(student.sort(),1):
#     print('번호:{}, 이름: {}'.format(n,name))