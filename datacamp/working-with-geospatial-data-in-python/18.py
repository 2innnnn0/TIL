# 18.py
# Join the districts and stations datasets

joined = geopandas.sjoin(stations,
                        districts,
                        op='within')

# Inspect the first five rows of the result
print(joined.head(5))

>> <script.py> output:
                                           name  bike_stands  available_bikes  \
    0                    14002 - RASPAIL QUINET           44                4   
    143  14112 - FAUBOURG SAINT JACQUES CASSINI           16                0   
    293               14033 - DAGUERRE GASSENDI           38                1   
    346     14006 - SAINT JACQUES TOMBE ISSOIRE           22                0   
    429       14111 - DENFERT-ROCHEREAU CASSINI           24                8   
    
                                            geometry  index_right  id district_name  
    0     POINT (450804.448740735 5409797.268203795)           52  53  Montparnasse  
    143   POINT (451419.446715647 5409421.528587255)           52  53  Montparnasse  
    293  POINT (450708.2275807534 5409406.941172979)           52  53  Montparnasse  
    346  POINT (451340.0264470892 5409124.574548723)           52  53  Montparnasse  
    429  POINT (451274.5111513372 5409609.730783217)           52  53  Montparnasse
