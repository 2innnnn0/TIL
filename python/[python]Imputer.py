
''' Python 누락정보값 채우기.
missing_values : 누락 정보
strategy : 채우는 방법. 디폴트는 "mean"
    "mean": 평균
    "median": 중앙값
    "most_frequent": 최빈값
'''


import numpy as np

from sklearn.preprocessing import Imputer
imp = Imputer(missing_values = 'NaN', strategy = 'mean', axis=0)

imp.fit_transform([[1,2],[np.nan, 3],[7,6]])
