# 21_choropleths.py

countries.plot(column='gdp_per_cat')

location.plot(column='variable')

# choropleth with classfication scheme.
location.plot(column='variable', scheme='quantiles', k=7, cmap='virids')
# number of classes : `k` -> detail하려면 k를 크게, abstrating 하려면 k를 작게
# classfication algorithm : `scheme -> equal_interval과 qunatiles 이 있음.
    # equal_interval은 bin사이즈가 균일하게 되는것(=qunatize), qunatiles은 데이터값을 비율에 맞게 biz사이즈가 상대적으로 조절.
    ex. location.plot(column='variable', scheme='equal_interval', k=7, cmap='virids')
# color palette : `cmap` 
    # 카테고리categorical와 연속형sequential(같은 색상), 구분도divergent
    # categorical
    location.plot(column='variable',
                 categorical=True,
                 cmap='Purples')
    #  sequential
    location.plot(column='variable',
                 k=5,
                 cmap='RdPu')
    # divergent
    location.plot(column='variable',
                 k=5,
                 cmap='RdY1Gn')