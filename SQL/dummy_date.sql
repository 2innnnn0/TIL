WITH time_windows AS (
SELECT
  TIMESTAMP_ADD(TIMESTAMP_TRUNC(first, HOUR), INTERVAL step MINUTE) AS DD
FROM (
  SELECT
    TIMESTAMP("2018-01-01", 'Asia/Seoul') AS first,
    TIMESTAMP("2018-01-02", 'Asia/Seoul') AS last),
  UNNEST(GENERATE_ARRAY(0, TIMESTAMP_DIFF(last, TIMESTAMP_TRUNC(first, HOUR), MINUTE), 60)) AS step)


select datetime(DD, 'Asia/Seoul') as DD
from 



-- 


#날짜변환
CREATE TEMP FUNCTION datetime_convert(timestamp TIMESTAMP) AS (
  DATETIME(timestamp ,"Asia/Seoul")
);

WITH time_windows AS (
SELECT
  DATETIME_ADD(DATETIME_TRUNC(first, HOUR), INTERVAL step MINUTE) AS DD
FROM (
  SELECT
    DATETIME("2018-01-01", 'Asia/Seoul') AS first,
    DATETIME("2018-01-02", 'Asia/Seoul') AS last),
  UNNEST(GENERATE_ARRAY(0, DATETIME_DIFF(last, DATETIME_TRUNC(first, HOUR), MINUTE), 60)) AS step)
 , time_windows2 as (
 SELECT
  TIMESTAMP_ADD(TIMESTAMP_TRUNC(first, HOUR), INTERVAL step MINUTE) AS DD
FROM (
  SELECT
    TIMESTAMP("2018-01-01", 'Asia/Seoul') AS first,
    TIMESTAMP("2018-01-02", 'Asia/Seoul') AS last),
  UNNEST(GENERATE_ARRAY(0, TIMESTAMP_DIFF(last, TIMESTAMP_TRUNC(first, HOUR), MINUTE), 60)) AS step)

select 
   DD as DD2
    , timestamp_ADD(DD, INTERVAL 1 hour)
from time_windows2
;