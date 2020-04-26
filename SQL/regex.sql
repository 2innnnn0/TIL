-- 전화번호
-- 차량번호 
with mem as (
select 
"""	
ㄴ 00하1234 / A드라이버 / 010-1111-2222
ㄴ 사고 사진은 등록했는데, 보험접수번호는 안 오는건지 문의
ㄴ 자차 보험이 없어 별도의 면책 제도 운용중에 있으며, 담당자 통해 면책 가능 여부 확인 후 안내 드리고 있음 안내
ㄴ 수긍 후 종료
""" as memo
)

select 

ARRAY_LENGTH(car_num)
, ARRAY_LENGTH(name)
, ARRAY_LENGTH(phone)
, ARRAY_LENGTH(agency)

from
(select 
-- 차량번호가 우리께 아니면, 제거하기
substr(memo, 
if(STRPOS(memo , '차량번호')=0, null, STRPOS(memo , '차량번호'))+4,10),
substr(memo, STRPOS(memo , '연락처')+3,17),
substr(memo, if(STRPOS(memo , '소속 업체')=0, null, STRPOS(memo , '소속 업체'))+5, 10),

regexp_extract_all(
substr(memo, 
if(STRPOS(memo , '차량번호')=0, null, STRPOS(memo , '차량번호'))+4,10)
, '([0-9]{2}[가-힣]{1}\\s{0,1}[0-9]{4})') as car_num
, 

regexp_extract_all(substr(memo, 
if(STRPOS(memo , '이름')=0, null, STRPOS(memo , '이름'))+2, 10), '[가-힣]{2,3}' ) as name,

regexp_extract_all(substr(memo,  if(STRPOS(memo , '연락처')=0, null, STRPOS(memo , '연락처')) +3, 17) ,  '010-?[0-9]{3,4}-?[0-9]{4}') as phone,

regexp_extract_all(substr(memo, if(STRPOS(memo , '소속 업체')=0, null, STRPOS(memo , '소속 업체'))+5, 10) ,  '([가-힣\\s]{3,8})') as agency

from mem
where 1=1
)