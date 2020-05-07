# 38_Styling a multi-layered plot.py

# Plot of the parks and mining sites
ax = national_parks.plot(color='green')
mining_sites.plot(ax=ax,markersize=5)
plt.show()


# Plot of the parks and mining sites
ax = national_parks.plot(color='green')
mining_sites.plot(ax=ax, column='mineral', legend=True, markersize=5, alpha=0.5)
ax.set_axis_off()
plt.show()