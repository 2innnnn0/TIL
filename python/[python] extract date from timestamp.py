# https://stackoverflow.com/questions/39662149/pandas-extract-date-and-time-from-timestamp

# I want to extract date and time from it. I have done the following:
# 2016-06-16T21:35:17.098+01:00
import datetime as dt


df['timestamp'] = df['timestamp'].apply(lambda x : pd.to_datetime(str(x)))
df['dates'] = df['timestamp'].dt.date

# This worked for a while. But suddenly it does not.
# If I again do df['dates'] = df['timestamp'].dt.date I get the following error

# Can only use .dt accessor with datetimelike values
# Luckily, I have saved the data frame with dates in the csv but I now want to create another column time in the format 23:00:00.051



