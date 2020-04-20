# 11_Shapely geometries and spatial relationships.py


# scalar geometry values
cities = geopandas.read_file('.shp')
cities.head()

brussels = cities.loc[170,'geometry'] # 170번째 인덱스에 위치해있는 것은 brussels의 위치다.
print(brussels)

type(brussels) 
>> shapely.geometry.point.Point

# Shapely
# 지리객체를 분석하는데 사용하는 파이썬 패키지
# Point, LineString, Polygon 객체가 있다.
# GeoSeries(GeoDataFrame 'geometry' 컬럼)는 Shapley의 객체다.


# Geometry Objects 

### 데이터에 접근해서 추출하기 
brussels = cities.loc[170, 'geometry']
uk = cities.loc[[countries['name']=='United Kingdom' , 'geometry'].squeeze()

### 임의로 만들기.
from shapely.geometry import Point
p = Point(1,2)
print(p)
>> POINT(1,2)


# Spatial Methods 

### geometry의 면적을 구할떄 
belgium.area
>> 3.82999..

### 두개의 geometry사이의 직선 distance를 구할떄
brussels.distance(paris)
>> 2.804..

### 그외에도 centrid, simplify 등 각종 지리함수들이 있음

# Spatial Releationships
geopandas.GeoSeries([belgium, france, uk, paris, brussels, line]).plot()


belgium.contains(brussels)
>> True

france.contains(brussels)
>> False 

brussels.within(belgium)
>> True

belgium.touches(france)
>> True 

line.intersects(france)
>> True

line.intersects(uk)
>> False 

