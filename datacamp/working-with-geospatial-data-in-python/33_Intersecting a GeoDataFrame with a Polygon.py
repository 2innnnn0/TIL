# 33_Intersecting a GeoDataFrame with a Polygon.py
# Print the land use datset and Notre-Dame district polygon
print(land_use.head())
print(type(muette))

# Calculate the intersection of the land use polygons with Notre Dame
land_use_muette = land_use.intersection(muette)

# Plot the intersection
land_use_muette.plot(edgecolor='black')
plt.show()

# Print the first five rows of the intersection
print(land_use_muette.head())
