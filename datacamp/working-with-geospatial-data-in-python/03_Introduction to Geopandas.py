# 03_Introduction to Geopandas.py

# 1. importing geospatial Data with geopandas
# geopandas는 geojson, shp파일 등을 지원한다.
# geopandas의 타입은 geopandas.geodataframe.GeoDataFrame 이다.
# geopandas. geometry로 하면 자동으로 지리데이터를 인식한다.
# geometry속성의 타입은 geopandas.geosereis.GeoSeires 이다.
# geometry.area 는 면적값을 float으로 반환한다.

# geoDataFrame은 판다스의 데이터프레임과 같다. 


import geopandas
contries = geopandas.read_file("contries.geojson")
contries.head()

# contries에서 
contries.plot()


