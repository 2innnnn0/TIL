# 10_Plotting multiple layers.py

# Load the restaurants dataset
restaurants = geopandas.read_file("paris_restaurants.geosjon")

# restaurants['type'].unique()

# Take a subset of the African restaurants
african_restaurants = restaurants[restaurants['type'] == 'African restaurant']

# Make a multi-layered plot
fig, ax = plt.subplots(figsize=(10, 10))
restaurants.plot(ax=ax, color='grey')
african_restaurants.plot(ax=ax, color='red')
# Remove the box, ticks and labels
ax.set_axis_off()
plt.show()


# countries.plot(ax=ax)
# cities.plot(ax=ax, color='red', markersize=10)
