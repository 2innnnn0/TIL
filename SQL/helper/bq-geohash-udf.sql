#standardSQL
CREATE TEMPORARY FUNCTION geohashDecode(geohash STRING)
RETURNS STRUCT<bbox ARRAY<FLOAT64>, lat FLOAT64, lng FLOAT64> 
  LANGUAGE js AS """
    if (!geohash) return null;
    var base32 = '0123456789bcdefghjkmnpqrstuvwxyz';
    geohash = geohash.toLowerCase();
    var evenBit = true;
    var latMin =  -90, latMax =  90;
    var lonMin = -180, lonMax = 180;
    for (var i=0; i<geohash.length; i++) {
        var chr = geohash.charAt(i);
        var idx = base32.indexOf(chr);
        if (idx == -1) throw new Error('Invalid geohash');
        for (var n=4; n>=0; n--) {
            var bitN = idx >> n & 1;
            if (evenBit) {
                // longitude
                var lonMid = (lonMin+lonMax) / 2;
                if (bitN == 1) {
                    lonMin = lonMid;
                } else {
                    lonMax = lonMid;
                }
            } else {
                // latitude
                var latMid = (latMin+latMax) / 2;
                if (bitN == 1) {
                    latMin = latMid;
                } else {
                    latMax = latMid;
                }
            }
            evenBit = !evenBit;
        }
    }
    var new_struct = new Object();
    new_struct.bbox = [latMin, lonMin, latMax, lonMax]; // Bounding Box
    new_struct.lat = (latMax + latMin) / 2; // Center Latitude
    new_struct.lng = (lonMax + lonMin) / 2; // Center Longitude
  
  return new_struct;
""";
SELECT geohashDecode(geohash) as doubles
FROM UNNEST(['u2ffwc9','u342633', null]) AS geohash;