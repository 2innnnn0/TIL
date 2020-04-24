with after_weather as (
  SELECT
        datetime(STCS_DATE) AS datetime_,
        CAST(TA AS float64) AS temperature,
        CAST(ifnull( RN,
            '0') AS float64) AS rain_amount,
        CAST(WS AS float64) AS windspeed,
        CAST(HM AS int64) AS humidity
      FROM
        `kma_after_local_weather_*`
      WHERE
        1=1
        AND _table_suffix <= format_datetime( '%Y%m%d' , current_datetime('Asia/Seoul'))
        AND stn_nm = '서울'
       )
       , time_windows AS (
SELECT
  DATETIME_ADD(DATETIME_TRUNC(first, HOUR), INTERVAL step MINUTE) AS DD
FROM (
  SELECT
    DATETIME("2018-10-08", 'Asia/Seoul') AS first ,
    datetime(date(  datetime_add(current_datetime('Asia/Seoul'), interval 3 day)  )) as last
    ) ,
  UNNEST(GENERATE_ARRAY(0, DATETIME_DIFF(last, DATETIME_TRUNC(first, HOUR), MINUTE), 60)) AS step),       

  before_weather AS (
      select
        datetime(fcstdatetime) as datetime_
        , round(avg(cast(T3H as float64)),1) as temperature
        , ifnull(round(avg(cast(R06 as float64)),1),0) as rain_amount
        , round(avg(cast(WSD as float64)),1) as windspeed -- ~4:없음  4~9  9~14 14~
        , round(avg(cast(REH as float64)),1) as humidity
        from `kma_before_local_weather_*` before
        where 1=1
        and date(fcstdatetime) >= current_date('Asia/Seoul')
        and region1 = '서울특별시'
        group by datetime_
        ,region1
        )
    
select tw.DD
, ifnull(after.temperature , ifnull(before.temperature, round(avg(before.temperature) over( ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING),1)) ) as temperature
, ifnull(after.rain_amount , ifnull(before.rain_amount, round(avg(before.rain_amount) over( ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING),1)) ) as rain_amount
, ifnull(after.windspeed , ifnull(before.windspeed, round(avg(before.windspeed) over( ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING),1)) )  as windspeed
, ifnull(after.humidity , ifnull(before.humidity, round(avg(before.humidity) over( ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING),1)) ) as humidity
from time_windows tw 
  left join before_weather before
    on tw.DD = before.datetime_
  left join after_weather after
    on tw.DD = after.datetime_