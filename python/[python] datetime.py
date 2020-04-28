# 기본적인 기능
import datetime
datetime.datetime.strptime('2018-10-11', '%Y-%m-%d')
datetime.datetime(2018,10,11)


import datetime
import numpy as np

data = np.array(
    [[2015, 2015, 2015, 2015, 2015, 2015],
     [   1,    1,    1,    1,    1,    1],
     [   1,    1,    1,    2,    2,    2],
     [  23,   23,   23,    0,    0,    0],
     [   4,    5,    5,   37,   37,   37],
     [  59,    1,    2,   25,   27,   29]]
)

# Transpose the data so that columns become rows.
data = data.T

# A simple list comprehension does the trick, '*' making sure
# the values are unpacked for 'datetime.datetime'.
new_data = [datetime.datetime(*x) for x in data]

print(new_data)


# ============================================================
import pandas
df['created_at'] = pd.to_datetime(df['created_at'])
df['year'] = df['created_at'].dt.year
df['month'] = df['created_at'].dt.month
df['day'] = df['created_at'].dt.day
df['date'] = df['created_at'].dt.date
df['time'] = df['created_at'].dt.time
df['quarter'] = df['created_at'].dt.quarter
df['weekday'] = df['created_at'].dt.weekday
df['hour'] = df['created_at'].dt.hour
df['created_at'] = pd.to_datetime(df['created_at']) + pd.DateOffset(hours=9)
df['created_at_30min'] = df['created_at'].dt.floor("30min")
df['created_at_hour'] = df['created_at'].dt.round("H")


df['weekday'] = df['weekday'].astype('str')
df['hour'] = df['hour'].astype('str')

# ============================================================
# 각 요소들을 합해서 새로운 날짜

df['datetime'] = (df['date'] + ' '+ pd.to_datetime(df['hour'],format='%H').dt.time.astype(str))

# ============================================================
