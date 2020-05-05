# 30_Projecting to Web Mercator for using web tiles.py

# Convert to the Web Mercator projection
restaurants.crs
restaurants_webmercator = restaurants.to_crs(epsg=3857)

# Plot the restaurants with a background map
ax = restaurants_webmercator.plot(markersize=1)
contextily.add_basemap(ax)
plt.show()