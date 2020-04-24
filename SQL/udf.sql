# H3
CREATE TEMP FUNCTION geo_to_h3(lat FLOAT64, lng FLOAT64, resolution INT64) RETURNS STRING LANGUAGE js AS
'''return h3.geoToH3(lat, lng, resolution)''' OPTIONS ( library=["gs://udf/h3.js"] );

CREATE TEMP FUNCTION h3_to_geo( h_idx STRING) RETURNS STRING LANGUAGE js AS
'''return h3.h3ToGeo(h_idx)''' OPTIONS ( library=["gs://udf/h3.js"] );
