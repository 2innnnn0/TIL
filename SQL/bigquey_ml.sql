 WITH
  Distances AS (
  SELECT
    DISTINCT ML.CENTROID_ID,
    sepal_length,
    sepal_width,
    petal_length,
    petal_width,
    species,
    MIN(NEAREST_CENTROIDS_DISTANCE.DISTANCE) AS distance_from_closest_centroid
  FROM
    ML.PREDICT(MODEL dataset.iris_clusters, 
      (
      SELECT
        DISTINCT sepal_length,
        sepal_width,
        petal_length,
        petal_width,
        species
      FROM
        `bigquery-public-data.ml_datasets.iris`  )) AS ML
  CROSS JOIN
    UNNEST(NEAREST_CENTROIDS_DISTANCE) AS NEAREST_CENTROIDS_DISTANCE
  GROUP BY
    ML.CENTROID_ID,
    sepal_length,
    sepal_width,
    petal_length,
    petal_width,
    species )

,Threshold AS (
  SELECT
    ROUND(APPROX_QUANTILES(distance_from_closest_centroid,10000)[
    OFFSET
      (9500)],2) AS threshold
  FROM
    Distances)
    
    SELECT
  d.*
FROM
  Distances d
JOIN
  Threshold
ON
  d.distance_from_closest_centroid > Threshold.threshold