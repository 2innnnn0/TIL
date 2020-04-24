-- 위경도 직선거리Km UDF
CREATE TEMP FUNCTION RADIANS(x FLOAT64) AS (
  ACOS(-1)*x/180
);
CREATE TEMP FUNCTION RADIANS_TO_KM(x FLOAT64) AS (
  (111.045*180)*x/ACOS(-1)
);
CREATE TEMP FUNCTION HAVERSINE(lat1 FLOAT64, long1 FLOAT64,
                               lat2 FLOAT64, long2 FLOAT64) AS (
  RADIANS_TO_KM(SAFE.ACOS(COS(RADIANS(lat1)) * COS(RADIANS(lat2)) *
         COS(RADIANS(long1) - RADIANS(long2)) +
         SIN(RADIANS(lat1)) * SIN(RADIANS(lat2))))
         
);

CREATE TEMP FUNCTION DISTANCE_FROM_ZONE(lat1 FLOAT64, long1 FLOAT64,
                                         lat2 FLOAT64, long2 FLOAT64) as (
  HAVERSINE(round(lat1,8), round(long1,8)
           ,round(lat2,8) , round(long2,8))
)
;

