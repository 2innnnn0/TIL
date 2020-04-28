

df['gu'] = df['address'].apply(lambda x: x.split(" ")[1])
