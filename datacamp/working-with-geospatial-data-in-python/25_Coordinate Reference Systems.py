# 25_Coordinate Reference Systems.py

# CRS개념
POINT (2.2945, 48.8584)


# 파이썬에서 위경도 좌표 입력순서.
- (lon, lat)임. 

# 위경도의 범위
LONG [-180, 180] 
LAT [-90, 90]

# 우리의 지도는 2D로 표현하지만, 실제로는 많이 왜곡되어있다.
# projected Coordinates
    - 3D상으로 되어있는 값(lon, lat) -> 2D의 평면의 좌표값(x,y)로 변환하는 작업. (meter로 표현)
    - 우리는 mercator projector를 사용.

# Specifying a CRS 
- `proj4` string (발음은 프로_포)
    ex. +proj=longlat +datum=WGS84 +no_defs
    Dict Representation:
    {'proj':'longlat','datum':'WGS84','no_defs':True}
- EPGS code
    ex. EPSG:4326 = WGS84 geographic CRS (long, lat)


# CRS in GeoPandas
import geopandas 
gdf = geopandas.read_file('contries.shp')
print(gdf.crs)
>> {'init':'epsg:4326'}


# Summary 
- geographic(long,lat)과 Projected(x,y) 죄표계의 차이 구분하기.
- CRS in geopandas : `.crs` 속성
- 대표적인 좌표계는 WGS84 / EPSG4236