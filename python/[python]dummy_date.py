# dummy data 생성
def dummydata():
    start = dt.datetime(2018,10,8)
    end = dt.datetime(2019,12,31)
    step = dt.timedelta(days=1)
    weekday = start.weekday()
    DD = []
    while start <= end:
        DD.append([dt.datetime.strftime(start, '%Y-%m-%d'),start.weekday()])
        start +=step
    # 구별 일,요일별, 시간대별 더미 데이터 밑밥
#     gu = full_df['gu'].unique()
    gu = ['강남구', '강동구', '강서구', '관악구', '광진구', '구로구', '금천구', '동대문구', '동작구',
       '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구',
       '은평구', '종로구', '중구', '도봉구', '강북구', '노원구', '중랑구']
    gu = pd.DataFrame(gu, columns=['gu'])
    gu['key']=1

    DD = pd.DataFrame(DD, columns=['date','weekday'])
    DD['key']=1
    hour = pd.DataFrame(list(range(0,24)), columns=['hour'])
    hour['key']=1

    merge_df = pd.merge( gu , DD , on='key').drop('key', axis=1)
    merge_df['key']=1
    drop_df = pd.merge( merge_df , hour , on='key').drop('key', axis=1)

#     drop_df['weekend'] = 'weekday'
#     drop_df['weekend'][(drop_df['weekday_num']==5)|(drop_df['weekday_num']==6)] = 'weekend'

    #am/pm추가
#     drop_df['ampm']='pm'
#     drop_df['ampm'][drop_df['hour']<=11] = 'am'

    #peak추가
#     when cast(format_datetime( "%u" , cast(created_at_kr as datetime)) as int64) in (2,3,4,5,6) and EXTRACT(HOUR FROM cast(created_at_kr as datetime)) in (0,1,2,8,9,18,19,22,23) then 'peak' -- 화~금
#     when cast(format_datetime( "%u" , cast(created_at_kr as datetime)) as int64 )in ( 1 ) and EXTRACT(HOUR FROM cast(created_at_kr as datetime)) in (8,9,18,19,22,23) then 'peak' -- 월
#     when cast(format_datetime( "%u" , cast(created_at_kr as datetime)) as int64) in ( 7 ) and EXTRACT(HOUR FROM cast(created_at_kr as datetime)) in (0,1,2) then 'peak' -- 일


#     drop_df['peak']='normal'
#     drop_df['peak'][(drop_df['hour']==8)|(drop_df['hour']==9)|(drop_df['hour']==18)|(drop_df['hour']==22)|(drop_df['hour']==23)|(drop_df['hour']==0)|(drop_df['hour']==1)|(drop_df['hour']==2)] = 'peak'

    return drop_df











#


import datetime as dt
import pandas as pd
def dummydata():
    start = dt.datetime(2018,10,8)
    end = dt.datetime(2019,12,31)
    step = dt.timedelta(days=1)
    weekday = start.weekday()
    DD = []
    while start <= end:
        DD.append([dt.datetime.strftime(start, '%Y-%m-%d'),start.weekday()])
        start +=step
    gu = ['강남구', '강동구', '강서구', '관악구', '광진구', '구로구', '금천구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '도봉구', '강북구', '노원구', '중랑구']
    gu = pd.DataFrame(gu, columns=['gu'])
    gu['key']=1
    DD = pd.DataFrame(DD, columns=['date','weekday'])
    DD['key']=1
    hour = pd.DataFrame(list(range(0,24)), columns=['hour'])
    hour['key']=1
    merge_df = pd.merge( gu , DD , on='key').drop('key', axis=1)
    merge_df['key']=1
    merge_df = pd.merge( merge_df , hour , on='key').drop('key', axis=1)
    return merge_df


dummydata()
