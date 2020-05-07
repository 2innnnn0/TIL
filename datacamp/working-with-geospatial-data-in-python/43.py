# 43_Working with raster data.py
# vector와 raster 



# 1. The rasterio package
import rasterio
- "pythonic" bindings to GDAL 
- reading and writing raster files
- processing tools (masking, reprojection, resampling)
rasterio.readthedocs.io 참고

# 2. opening a raster file

import rasterio
src = rasterio.open("DEM_world.tif")

Metadata
src.count, src.width, src.height 로 raster데이터의 특징을 알 수 있다

# 3. raster data = numpy array
array = src.read() # numpy 로 다룰 수 있음. 
array


# 4. plotting a raster datasets
import rasterio.plot
rasterio.plot.show(src, cmap='terrain')



# 5. extract raster values with rasterstats
# https://github.com/perrygeo/python-rasterstats
import rasterstats
# for point vectors
rasterstats.point_query(geometries, "path/to/raster",
                        interpolation='nearest'|'bilinear')
                        
# for polygon vectors
rasterstats.zonal_stats(geometries, "path/to/raster",
                        stats=['min','mean','max'])


result = rasterstats.zonal_stats(countries.geometry, "DEM_gworld.tif",
                                stats=['mean'])
countries['mean_elevation'] = pd.DataFrame(result)
countries.sort_values('mean_elevation', ascending=False).head()


