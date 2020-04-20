# 04_Explore the Paris districts (I).py

# Import GeoPandas
import geopandas

# Read the Paris districts dataset
districts = geopandas.read_file("paris_districts.gpkg")

# Inspect the first rows
print(districts.head(5))

# Make a quick visualization of the districts
districts.plot()
plt.show()