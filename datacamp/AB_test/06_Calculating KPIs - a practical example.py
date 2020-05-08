# 06_Calculating KPIs - a practical example.py

# conversion rate : maximum lapse date

import pandas as pd
from datetime import datetime, timedelta

current_date = pd.to_datetime('2018-03-17')

- lapse date : date the trial ends for a given user 지정된 사용자에 대한 종료 날짜
print(sub_data_demo.lapse_date.max())
>> '2018-03-17'

# KPI calculation : restrict users by lapse date

### latest lapse date : a week before today
max_lapse_date = current_date - timedelta(days=7)

### restrict to users lapsed before max_lapse_date 
conv_sub_data = sub_data_demo[(sub_data_demo.lapse_date < max_lapse_date)]

### count the users remaining in our data
total_users_count = conv_sub_data.price.count()
print(total_users_count)
>> 2787



# Cohort conversion rate
sub Time : how long it took a user to subscribe 


