# 37_Convert to common CRS and save to a file.py

# Plot the natural parks and mining site data
ax = national_parks.plot()
mining_sites.plot(ax=ax, color='red')
plt.show()

# Convert both datasets to UTM projection
mining_sites_utm = mining_sites.to_crs(epsg=32735)
national_parks_utm = national_parks.to_crs(epsg=32735)

# Plot the converted data again
ax = national_parks_utm.plot()
mining_sites_utm.plot(ax=ax, color='red')
plt.show()

# Write converted data to a file
mining_sites_utm.to_file("ipis_cod_mines_utm.gpkg",driver='GPKG')
national_parks_utm.to_file("cod_conservation_utm.shp",driver='ESRI Shapefile')