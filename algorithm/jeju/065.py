# 065.py
# a=[1,2,3,4]
# b=[a,b,c,d] 리스트가 입력되면, 
# [[1,a],[b,2],[3,c],[d,4]] a,b리스트가 번갈아가면서 출력되게 하기

a=[1,2,3,4]
b=['a','b','c','d']

# result = []
# for i in range(len(a)):
#     result.append([a[i],b[i]])
# print(result)

# SOL
c = []
count = 0

for i,j in zip(a,b):
    # print(i,j)
    if count % 2 == 0:
        c.append([i,j])
    else:
        c.append([j,i])
    count += 1
print(c)