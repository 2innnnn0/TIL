with parse as (
select
JSON_EXTRACT_SCALAR('[{“rfer_desc”:“\uc0ac\uace0\uc0c1\ud669:\uc0ac\uace0\uc0c1\ud669\ud14c\uc2a4\ud2b8  \ud30c\uc190\ubd80\uc704:\ud30c\uc190\ubd80\uc704\ud14c\uc2a4\ud2b8}]', '$.rfer_desc') AS rfer_desc

)
, encode as (
SELECT a, b, a = b as normalized
FROM (SELECT NORMALIZE('\u00ea') as a, NORMALIZE('ê') as b, NORMALIZE('\uc0ac\uace0\uc0c1\ud669:\uc0ac\uace0\uc0c1\ud669\ud14c\uc2a4\ud2b8') as c) AS normalize_example

)

select *
from encode
