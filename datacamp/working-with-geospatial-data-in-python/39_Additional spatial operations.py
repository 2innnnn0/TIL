# 39_Additional spatial operations.py

# buffer Operation 
- point.buffer(distance)
- line.buffer(distance)
- polygon.buffer(distance)


# goma is a Point
print(type(goma))

# Create a buffer of 50km around Goma
goma_buffer = goma.buffer(50000)

# The buffer is a polygon
print(type(goma_buffer))

# Check how many sites are located within the buffer
mask = mining_sites.within(goma_buffer)
print(mask.sum())

# Calculate the area of national park within the buffer
print(national_parks.intersection(goma_buffer).area.sum() / (1000**2))




# ======= HINT
The `buffer()` method takes the buffer distance as argument, which should be expressed in meters (the unit of the CRS).
Remember the `within()` method. It checks for each geometry if it is located within the specified polygon.
Remember the `intersection()` method to calculate the intersection of each geometry of the GeoDataFrame with the specified geometry.