select h3_idx, 
    count(case when biz.category1 = '숙박' then biz.id end) as biz_inn_count,
    count(case when biz.category1 = '관광/여가/오락' then biz.id end) as biz_amuse_count,
    count(case when biz.category1 = '음식' and biz.category2 in ('유흥주점') then biz.id end) as biz_food_count,
    count(case when biz.category1 = '소매' then biz.id end) as biz_retail_count,
    count(case when biz.category1 = '생활서비스' and biz.category2 in ('이/미용/건강', '주유소/충전소', '대중목욕탕/휴게' , '예식/의례/관혼상제', '행사/이벤트', '개인/가정용품수리')
            then biz.id end) as biz_lifeservice_count,
    count(case when biz.category1 = '의료' then biz.id end) as biz_medical_count,
    count(case when biz.category1 = '스포츠' then biz.id end) as biz_sports_count,
    count(case when biz.category1 = '학문/교육' then biz.id end) as biz_academy_count
    from
    (
        select * ,
            geo_to_h3(lat,lng, 8) as h3_idx
        from `gis.biz_region` biz
        where biz.region1 = '인천광역시'
    ) biz
group by 1