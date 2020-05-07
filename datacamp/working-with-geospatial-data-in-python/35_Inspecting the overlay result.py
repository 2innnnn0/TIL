# 35_Inspecting the overlay result.py
# Print the first rows of the overlay result
print(combined.head(2))

# Add the area as a column
combined['area'] = combined.geometry.area

# Take a subset for the Muette district
land_use_muette = combined[combined['district_name']=='Muette']
land_use_muette

# Visualize the land use of the Muette district
land_use_muette.plot(column='class')
plt.show()

# Calculate the total area for each land use class
print(land_use_muette.groupby('class')['area'].sum() / 1000**2)
