# 02_Adding a background map.py

# Read the restaurants csv file
restaurants = pd.read_csv("paris_restaurants.csv")

# Import contextily
import contextily

restaurants.head()

# A figure of all restaurants with background
fig, ax = plt.subplots()
ax.plot(restaurants['x'], restaurants['y'], 'o', markersize=1)
contextily.add_basemap(ax)
plt.show()



# ---
# contextily패키지에서 add_basemap()는 백그라운드 맵을 쉽게 그려주는 함수다. 