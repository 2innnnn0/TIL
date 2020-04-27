-- 2019-05-21 특정 지역의 링크만 가져오고 싶을때
-- 활용예시는 -> 지역별 도로데이터 활용 

# 서울 : 100 ~ 124
# 부산 : 130 ~ 145
# 대구 : 150 ~ 157
# 인천 : 161 ~ 170
# 광주 : 175 ~ 179
# 대전 : 183 ~ 187
# 울산 : 192 ~ 196
# 경기 : 200 ~ 240

select wkt, LINK_ID,	F_NODE,	T_NODE, ROAD_NAME, code.REGION1 , code.region2, code.REGION_CODE , code.STNL_REG 
from `gis.moct_link_all` link
  join `gis.moct_region_code` code
    on link.STNL_REG = code.STNL_REG
where 1=1
and region1 = '인천광역시'


-- 

select 
    geometry,
    highway,
    key,
    length,
    name,
    oneway,
    osmid,
    u,
    v
from `gis.incheon_osm_link` 
where 1=1
and highway in 
    ('residential'
    ,'secondary'
    ,'tertiary'
    ,'unclassified'
    ,'primary'
    ,'living_street'
    ,'primary_link'
    ,'trunk_link'
    ,'secondary_link'
    ,'trunk'
    ,'motorway_link'
    ,'motorway'
    ,'tertiary_link'
    , 'road')