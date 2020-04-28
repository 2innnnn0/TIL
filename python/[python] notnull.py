
df = df[~((df['picked_up_at'].notnull()) & (df['cancellation_cause'] == 'cause1'))]


# drop
df = df.drop(df[(df['gu'] == '용산구') & (df['date'] == datetime.date(2018, 10, 28))].index)
print(df.shape)


drop_df = df[['id', 'created_at_30min','gu', 'status']].drop_duplicates(['id', 'created_at_30min','gu'], keep='last').groupby(['created_at_30min', 'id','gu', 'status']).count().reset_index()

# value_counts()
df[df['gu'] == '용산구'].groupby('gu')['date'].value_counts()

# 
df = df[~df['id'].isin(incorrect_id)]
