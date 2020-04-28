
# drop 
driver_cancel_outlier_index =
df[(df['']=='')
        & (df[''].notnull()==True)
        & (df[''].isnull()==True)].index
df = df.drop(driver_cancel_outlier_index)
df = df[df['gu'] != '과천시']
