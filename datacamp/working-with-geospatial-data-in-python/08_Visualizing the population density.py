# Inspect the first rows of the districts dataset
print(districts.head())

# Inspect the area of the districts
print(districts.geometry.area)

# Add a population density column
districts['population_density'] = districts.population / districts.geometry.area * (10**6)

# Make a plot of the districts colored by the population density
districts.plot('population_density', legend=True)
plt.show()