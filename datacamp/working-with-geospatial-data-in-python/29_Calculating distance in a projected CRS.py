# 29_Calculating distance in a projected CRS.py

# Extract the single Point
eiffel_tower = s_eiffel_tower_projected[0]

# s_eiffel_tower = geopandas.GeoSeries([eiffel_tower], crs={'init': 'epsg:4326'})
# s_eiffel_tower.crs

# Ensure the restaurants use the same CRS
restaurants = restaurants.to_crs({'no_defs': True, 'init': 'epsg:2154'})

# The distance from each restaurant to the Eiffel Tower
dist_eiffel = restaurants.distance(eiffel_tower)

# The distance to the closest restaurant
print(dist_eiffel.min())