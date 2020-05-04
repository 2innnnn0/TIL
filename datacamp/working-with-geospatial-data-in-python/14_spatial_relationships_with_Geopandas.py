# 14_spatial_relationships_with_Geopandas.py


# element-wise spatial relationship methods.
brussels.within(france)
>> False

paris.within(france)
>> True

cities.head()

# The within() operation for each geometry in cities:
# Data시리즈로 비교하는것과 인덱스로 하나씩 비교 하는 내용.


# 
# france를 포함하는 도시들 모음 
cities[cities.within(france)]

# 공간 관계로 필터링
within
contains
intersects

https://shapely.readthedocs.io/en/latest/ 참고하기