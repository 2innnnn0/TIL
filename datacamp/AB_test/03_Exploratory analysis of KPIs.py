# 03_Exploratory analysis of KPIs.py

# calculating KPIs
`pandas.DataFrame.groupby()`
`pandas.DataFrame.agg()`



# groupby()
- by : 그룹을 묶을 단위
- axis : 그룹을 묶을 축. 0=columns, 1=rows
- as_index : True는 그룹라벨을 인덱스로 사용

sub_data_grp = sub_data_demo.groupby(by=['country','device'],
                                    axis=0,
                                    as_index=False)
sub_data_grp 
>> DataFrameGroupby 로 리턴.


# agg()
- Mean price paid for each country / device 
sub_data_grp.price.mean()
>> 결과값은 나라와 기기에 따른 평균치 값을 보여줌

동일한 결과로 쓸수있는게
sub_data_grp.price.agg('mean')

다양한 집계값을 보고 싶다면,
sub_data_grp.price.agg(['mean','median'])

컬럼별로도 다른 집계를 볼수도 있다.
sub_data_grp.agg({'price' : ['mean','min','max'],
                'age' : ['mean','min','max']})

혹은 커스텀하게 사용을 한다면, 아래와 같이 적을 수 있다.
def truncated_mean(data):
    """compute the mean excluding outliers"""
    top_val = data.quntile(.9)
    bot_val = data.quntile(.1)
    trunc_data = data[(data <= top_val) & (data >= bot_val)]
    mean = trunc_data.mean()
    return(mean)

#find the truncated mean age by group
sub_data_grp.agg({'age':[truncated_mean]})

