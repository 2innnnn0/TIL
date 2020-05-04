# 16_How far is the closest restaurant?.py


# The distance from each restaurant to the Eiffel Tower

# type(restaurants)
# >> geopandas.geodataframe.GeoDataFrame
# restaurants.head() # restaurants데이터는
# >>                                  type                                     geometry
# 0                 European restuarant  POINT (259641.6916457232 6251867.062617987)
# 1       Traditional French restaurant  POINT (259572.3396029567 6252029.683163137)
# 2       Traditional French restaurant  POINT (259657.2763744336 6252143.400946027)
# 3  Indian / Middle Eastern restaurant  POINT (259684.4383301869 6252203.137238394)
# 4       Traditional French restaurant  POINT (259597.9430858413 6252230.044091299)
dist_eiffel = restaurants.distance(eiffel_tower)
# eiffel_tower.distance(restaurants)가 정답이 아닌 이유가 있나? - 에펠탑(geometry)으로 부터 레스토랑(series)까지의 거리. 

dist_eiffel

type(dist_eiffel)

# The distance to the closest restaurant
print(dist_eiffel.min())

# Filter the restaurants for closer than 1 km
restaurants_eiffel = restaurants[dist_eiffel<1000]


# Make a plot of the close-by restaurants
ax = restaurants_eiffel.plot()
geopandas.GeoSeries([eiffel_tower]).plot(ax=ax, color='red')
contextily.add_basemap(ax)
ax.set_axis_off()
plt.show()