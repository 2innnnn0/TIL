# 19_Map of tree density by district (1).py

# Read the trees and districts data
trees = geopandas.read_file("paris_trees.gpkg")
districts = geopandas.read_file("paris_districts_utm.geojson")

# Spatial join of the trees and districts datasets
joined = geopandas.sjoin(trees, districts, op='within')

# joined.head(1)
# joined['district_name']
# joined.district_name

# Calculate the number of trees in each district
trees_by_district = joined.groupby('district_name').count()['id']

# Convert the series to a DataFrame and specify column name
trees_by_district = trees_by_district.to_frame(name='n_trees')

# Inspect the result
print(trees_by_district.head())

>> script.py> output:
                     n_trees
    district_name           
    Amérique             183
    Archives               8
    Arsenal               60
    Arts-et-Metiers       20
    Auteuil              392