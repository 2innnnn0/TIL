# 09_Using pandas functionality: groupb.py

# Load the restaurants data
restaurants = geopandas.read_file("paris_restaurants.geosjon")

# Calculate the number of restaurants of each type
type_counts = restaurants.groupby('type').size() # .count() 가 아니다. 

# Print the result
print(type_counts)