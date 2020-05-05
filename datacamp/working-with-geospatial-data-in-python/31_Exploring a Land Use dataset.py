# 31_Exploring a Land Use dataset.py
# Import the land use dataset
land_use = geopandas.read_file('paris_land_use.shp')
print(land_use.head())

# Make a plot of the land use with 'class' as the color
land_use.plot('class', legend=True, figsize=(15, 10))
plt.show()

# Add the area as a new column
land_use['area'] = land_use.geometry.area

# Calculate the total area for each land use class
total_area = land_use.groupby('class')['area'].sum() / 1000**2
print(total_area)