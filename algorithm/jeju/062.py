# 062.py
# 20191011 을 출력
# 아래 기준 충족시키기
# 1. 코드 내에 숫자가 없어야함 (e.g. print(20191011)이라고 하면 안됨.)
# 2. 파일 이름이나 경로를 사용해서는 안된다.
# 3. 시간, 날짜 함수를 사용해서는 안된다.
# 4. 에러 번호 출력을 이용해서는 안된다.
# 5. input을 이용해서는 안된다.

# 20191011
# SOL
# 문자열의 갯수를 세는 방법으로 접근.
s= 'bccddddddddd'
print(s.count('a')) # 0
print(s.count('b')) # 1
print(s.count('c')) # 2
print(s.count('d')) # 9

print(s.count('c'), end='')
print(s.count('a'), end='')
print(s.count('b'), end='')
print(s.count('d'), end='')
print(s.count('b'), end='')
print(s.count('a'), end='')
print(s.count('b'), end='')
print(s.count('b'))