select 
  parse_datetime("%Y%m%d%k" , concat(cast(speed.observe_date as string), cast(speed.time-1 as string) ) ) as datetime_parse
  , speed.observe_date 
  , speed.time as hour
  , t1.service_id 
  , t1.ROAD_NAME 
  , speed.traffic 
from 
(select 
cast(round(link.LINK_ID,-2) as int64) service_id
, link.ROAD_NAME 
, st_union_agg( st_geogfromtext(link.wkt_geom)) as wkt_geom
from `gis.STD_LINK` link
group by
service_id
, link.ROAD_NAME
) t1
  join `gis.seoul_speed_201901` speed
    on t1.service_id = speed.link_id 
where speed.observe_date = 20190110