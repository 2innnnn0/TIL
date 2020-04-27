# H3
CREATE TEMP FUNCTION geo_to_h3(lat FLOAT64, lng FLOAT64, resolution INT64) RETURNS STRING LANGUAGE js AS
'''return h3.geoToH3(lat, lng, resolution)''' OPTIONS ( library=["gs://udf/h3.js"] );

CREATE TEMP FUNCTION h3_to_geo( h_idx STRING) RETURNS STRING LANGUAGE js AS
'''return h3.h3ToGeo(h_idx)''' OPTIONS ( library=["gs://udf/h3.js"] );



# age_from_ssn
if(regexp_contains(front_ssn, '[0-9]{6}-[1-9]{1}'),
          safe.date_diff( current_date(), safe.parse_date('%Y%m%d', concat(
          case when cast(substr(front_ssn, -1) as int64) in (1, 2, 5, 6) then '19' else '20' end
          , substr(front_ssn, 1, 6))), year) + 1,
         null
      )

# gender_from_ssn
if(
    regexp_contains(front_ssn, '[0-9]{6}-[1-9]{1}'),
    case
       when mod(safe_cast(substr(front_ssn, -1) as int64), 2)=1 then 'male'
       when mod(safe_cast(substr(front_ssn, -1) as int64), 2)=0 then 'female'
       else null
    end,
    null
  )

  

# dayofweek
case extract(dayofweek from dt)
    when 1 then 'sun'
    when 2 then 'mon'
    when 3 then 'tue'
    when 4 then 'wed'
    when 5 then 'thu'
    when 6 then 'fri'
    when 7 then 'sat'
    else null
  end