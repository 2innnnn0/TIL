# 41_Applying custom spatial operations.py
# Get the geometry of the first row
single_mine = mining_sites.geometry[0]

# Calculate the distance from each national park to this mine
dist = national_parks.distance(single_mine)

# The index of the minimal distance
idx = dist.idxmin()

dist[idx]

# Access the name of the corresponding national park
closest_park = national_parks.loc[idx, 'Name']
print(closest_park)