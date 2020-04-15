# chap2. 지리공간정보 자료의 구조 Structure of GIS Data
# 2.1 지리공간정보 자료의 구조
  # 1) 지리공간정보 자료의 기본구조
  # 공간자료Spatial Data구조는 n차원의 공간에서 유저가 요구하는 기하구조를 구성하는 자료를 의미. 일반적으로 2차원, 3차원 기하구조. 
    # 가장 많이 쓰이는 공간자료 구조 형식은 ArcGIS에서 적용하고 있는 Shape File 형식이다.
  # 벡터자료 : 공간에서의 기하구조를 점, 선, 면으로 표현하는것
  # 래스터자료 : 공간상에서의 기하구조를 Grid Data(or Pixel Data)로 불리는 격자형 Cell로 구본된 공간형태로 표현하는 것.
  # 공간 자료구조는 벡터든, 래스터든 좌표와 기하구조를 나타내는 도형자료Graphical Data와 속성자료Attribute Data의 특성을 구분하여 포함하게 됨

  # 2) SP Class: Spatital Data and Methods Class
  # - SP class의 세부내용
    # CRS
    # DMS
    # GridTopology
    # Line / Lines
    # Polygon / Polygons
    # SpatialGrid
    # SpatialGridDataFrame

  # 3) CRS Class : Coordiate Reference System Class
  # - 좌표계는 100여종이 넘는다.


  pp 


# import lib
library(maptools)
library(rgdal)
library(sp)
library(tidyverse)

# set_point (coordinate)
lat = c(37.5124500, 37.47181547)
lng = c(126.9395002, 126.9514850)

ll = data.frame(longtitude = long, latitude = lat)

Line(corrds)


library(maptools)
library(raster)
alt <- getData(???alt???, country = ???PHL???)
adm <- getData(???GADM???, country = ???PHL???, leve = 1)
mar <- (adm[adm$NAME_1 == ???Marinduque???, ])
maralt <- crop(alt, mar)
persp(
  maralt,
  exp = 0.2,
  phi = 35,
  xlab = ???Longitude???,
  ylab = ???Latitude???,
  zlab = ???Elevation???
)
