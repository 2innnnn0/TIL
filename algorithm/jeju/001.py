# 1. 리스트의 삭제
# 다음 리스트에서 400,500을 삭제하는 코드를 입력
nums = [100,200,300,400,500]
nums

type(nums)

# 핵심: 리스트의 특성을 이해하고 있는지

# sol1 : 인덱싱
nums[0:3]

# sol2 : del함수
del nums[3:5]
nums

# sol3 : pop
nums.pop()
nums.pop()
print(nums)


# sol4 : remove
nums.remove(400)
nums.remove(500)
print(nums)