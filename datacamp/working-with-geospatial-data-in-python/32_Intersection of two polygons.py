# 32_Intersection of two polygons.py
# Plot the two polygons
geopandas.GeoSeries([park_boulogne, muette]).plot(alpha=0.5, color=['green', 'blue'])
plt.show()

# Calculate the intersection of both polygons
intersection = park_boulogne.intersection(muette)

# Plot the intersection
geopandas.GeoSeries([intersection]).plot()
plt.show()

# Print proportion of district area that occupied park
print(intersection.area / muette.area)