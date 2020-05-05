# 22.py
 # Print the first rows of the tree density dataset
print(districts_trees.head(1))

# Make a choropleth of the number of trees 
districts_trees.plot(column='n_trees', legend=True)
plt.show()

# Make a choropleth of the number of trees per area
districts_trees.plot(column='n_trees_per_area', legend=True)
plt.show()

# Make a choropleth of the number of trees 
districts_trees.plot(column='n_trees_per_area', scheme='equal_interval', legend=True)
plt.show() 