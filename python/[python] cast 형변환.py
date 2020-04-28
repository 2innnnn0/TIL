# https://stackoverflow.com/questions/25952790/convert-pandas-series-from-dtype-object-to-float-and-errors-to-nans

import pandas as pd


# object to float
s = pd.Series(['1','2','3','4','.'])
pd.to_numeric(s, errors='coerce')



pd.to_numeric(s, errors='coerce').fillna(0, downcast='infer')


# float to int
import math
math.floor(3.2)

df['x'].apply(lambda x: math.floor(x))



# astype
