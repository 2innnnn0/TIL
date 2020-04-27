-- (인천)빌딩정보와 상권정보의 연결쿼리
select 
build.wkt, build.USABILITY , build.BLD_NM , biz.* except(building_id) , cast(biz.building_id as NUMERIC)  as b_id
from `gis.ko_incheon_building`  build
  join `gis.biz_region`  biz
    on cast(build.BD_MGT_SN as NUMERIC) =  cast(biz.building_id as NUMERIC) 
where 1=1
and cast(BD_MGT_SN as NUMERIC) is not null
and biz.category2 = '유흥주점'