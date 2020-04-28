# cross join 방식
origin_gu_list = drop_df['gu'].unique()
origin_gu_list.sort()

weekday_list = drop_df['weekday'].unique()
weekday_list.sort()

hour_list = drop_df['hour'].unique()
hour_list.sort()


feature_array = [[x1, x2, x3] for x1 in origin_gu_list for x2 in weekday_list for x3 in hour_list]
feature_test_df = pd.DataFrame(feature_array, columns=['gu', 'weekday', 'hour'])
feature_test_df.to_csv('.csv', index=False)
