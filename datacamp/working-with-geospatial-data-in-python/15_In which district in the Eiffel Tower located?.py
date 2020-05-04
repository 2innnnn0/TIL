#15_In which district in the Eiffel Tower located?.py
# Construct a point object for the Eiffel Tower
eiffel_tower = Point(255422.6, 6250868.9)

# Create a boolean Series
mask = districts.contains(eiffel_tower)

# Print the boolean Series
print(mask.head())

# Filter the districts with the boolean mask
print(districts[mask==True])

>>        geometry
27  28  Gros-Caillou       25156  POLYGON ((257097.2898896902 6250116.967139574,...