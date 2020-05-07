# 36_Import and explore the data.py
# Import GeoPandas and Matplotlib
import geopandas
import matplotlib.pyplot as plt

# Read the mining site data
mining_sites = geopandas.read_file("ipis_cod_mines.geojson")

national_parks = geopandas.read_file('cod_conservation.shp')

# Print the first rows and the CRS information
print(mining_sites.head())
print(mining_sites.crs)

print(national_parks.head())
print(national_parks.crs)

# Make a quick visualisation
mining_sites.plot(column='mineral')
national_parks.plot()
plt.show()