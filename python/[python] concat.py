# 인덱스가 서로 같을때, 합치는 방법
# 기존 test값과 y_predict 값을 연결할 때

# 주의! test.shape, y_predict.shape가 동일하고, 같은 인덱스여야만 아래 코드가 작동
pd.concat( [test, y_predict] , axis=1)
