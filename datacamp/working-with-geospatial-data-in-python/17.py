# 17.py

barzil = countries.loc[22,'geometry']
cities[cities.within(barzil)]



# spatial join
- transferring attributes from ine layer to another based
on their spaital relationship 

# spaital join wuth GeoPandas

joined = geopandas.sjoin(cities,
                        countries[['name'.'geometry']],
                        op='within')

joinedl.head()


