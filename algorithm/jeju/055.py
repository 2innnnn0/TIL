# 055.py 하노이탑
# 난이도 ***** 매우 어려움

# 하노이탑 규칙 
# 1. 처음에 모든 원판은 A기둥에 꽂혀있다. (시작기둥A,보조기둥B,목표기둥C 세 기둥이 있다)
# 2. 모든 원판의 지름은 다르다
# 3. 원반은 세개의 기둥 중 하나에 반드시 꽂혀야 함
# 4. 자신보다 작은 원반 위에 큰 원반을 놓을 수 없다.
# 5. 한번에 하나의 원판(가장 위에 있는 원판)만을 옮길 수 있다.

# 원판이 1개 일때
    # 바로 A > C 로 가면된다.
# 원판이 2개 일떄
    # 총 3번을 거친다. A > B. A > C. B > C
# 원판이 3개 일때
    # A > C. A > B. C > B. A > C. B > A. B > C. A > C
    # 7번을 거침.
# 하노이 탑의 최소 원반 이동횟수 = (2**n)-1
# BigO-> 0(2**n)

# SOL 
원판의이동경로 = []
def 하노이(원반의수, 시작기둥, 목표기둥, 보조기둥):
    # 원판이 한개일 때에는 옮기면 됩니다.
    if 원반의수==1 :
        원판의이동경로.append([시작기둥,목표기둥])
        return None
    # 원반의 n-1개를 경유기둥으로 옮기고
    하노이(원반의수-1, 시작기둥, 보조기둥, 목표기둥)
    # 가장 큰 원반은 목표기둥으로
    원판의이동경로.append([시작기둥,목표기둥])
    # 경유기둥과 시작기둥을 바꿉니다
    하노이(원반의수-1, 보조기둥, 목표기둥, 시작기둥)

user_input = int(input())
하노이(user_input, 'A','C','B')

print(원판의이동경로)
print(len(원판의이동경로))