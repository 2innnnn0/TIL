# 042.py
# 42번

import datetime
date = datetime.date(2019,7,20).weekday()
time = datetime.time(11,40,10)
print(date,time)


m = int(input())
d = int(input())
date = datetime.date(2020, m ,d).weekday()
dict_ = {1:'SUN', 2:'MON', 3:'TUE', 4:'WED', 5:'THU', 6:'FRI', 7:'SAT'}

dict_.keys()
dict_[date]