# 26_Working with coordinate systems in GeoPandas.py

# geoseries 
import geopandas
gdf = geopandas.read_file('countries.shp')
print(gdf.crs)
>> {'init':'epsg:4326'}

# setting CRS manually 수동으로 좌표계 설정하기.
gdf_noCRS = geopandas.read_file('countries_noCRS.shp')
print(gdf_noCRS)
>> {}
    # option1 
    gdf.crs = {'init':'epsg:4326'}

    # option2 
    gdf.crs = {'proj':'longlat','datum':'WGS84', 'no_defs':True}

# Transforming to Another CRS 다른 좌표계로 변환하는 방법 . `to_crs()`
    # option1 : 
    gdf2 = gdf.to_crs({'proj':'longlat','datum':'WGS84','no_defs':True})
    # option2 : shortcut
    gdf2 = gdf.to_crs(epsg=4326)


# why convering the CRS : 좌표계를 바꾸는 이유 
 -1.  여러 데이터셋들을 사용하다보면 서로 다른 좌표계를 사용할 떄가 발생할 수 있다. 
 이를 해결하기 위해 좌표계를 하나로 통일하기
df1 = geopandas.read_file(...)
df2 = geopandas.read_file(...)
df2 = df2.to_crs(df1.crs)
 - 2. 맵핑 
    - 서로 다른 좌표계는 공간계산을 할때 문제가 발생
 - 3. 거리 계산

# how to choose which CRS to use 
- 표준 CRS를 사용하면 된다. 끗
    - 참고할 좌표계 관련 정보
    - http://spaitialreference.org
    - https://epsg.io