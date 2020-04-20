# 07_Exploring and visualizing spatial_data.py


## filtering Data
countries.head()
countries['conitenet'] == 'Africa'
countries_africa = countries[countries['conitenet'] == 'Africa']
countries_africa.plot()


## visualizing spaitial data
countries.plot()

## uniform color
countries.plot(color='red')

## based on attribute value
countries.plot(columns='gdp_per_cap')


## multi_layerd plot
fig, ax = plt.subplots(figsize=(12,6))
countries.plot(ax=ax)
cities.plot(ax=ax, color='red', markersize=10)
ax.set_axis_off()