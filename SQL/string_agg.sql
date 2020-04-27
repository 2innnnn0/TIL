select
ST_ASGEOJSON(st_makeline(array_agg(geom_point))) as geojson
st_astext(st_makeline(array_agg(geom_point))) as geotext
from
(
  select
  , st_geogpoint(lng,lat) as geom_point
  from `coordinate` e
)  
  